from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import ChessGame, Move
from .serializers import ChessGameSerializer, MoveSerializer

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
