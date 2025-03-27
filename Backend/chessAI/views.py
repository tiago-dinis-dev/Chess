from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from .models import ChessGame, Move
from .serializers import ChessGameSerializer, MoveSerializer
from .ai_logic import select_best_move
import chess

class ChessGameViewSet(viewsets.ModelViewSet):
    queryset = ChessGame.objects.all().order_by('-created_at')
    serializer_class = ChessGameSerializer

    @action(detail=False, methods=['post'])
    def start_game(self, request):
        game = ChessGame.objects.create(player_white=request.data.get('player_white'), player_black=request.data.get('player_black'))
        serializer = self.get_serializer(game)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['patch'])
    def update_status(self, request, pk=None):
        game = self.get_object()
        new_status = request.data.get('status')
        game.update_status(new_status)
        return Response({'status': 'status updated'}, status=status.HTTP_200_OK)

class MoveViewSet(viewsets.ModelViewSet):
    queryset = Move.objects.all()
    serializer_class = MoveSerializer

class AIMoveView(APIView):

    def post(self, request, *args, **kwargs):

        board_state = request.data.get('board')
        board = chess.Board(board_state)
        
        best_move = select_best_move(board)
        
        board.push(best_move)
        return Response({'board': board.fen(), 'best_move': best_move.uci()})
