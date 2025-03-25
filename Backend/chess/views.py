from rest_framework import viewsets
from .models import ChessGame, Move
from .serializers import ChessGameSerializer, MoveSerializer

class ChessGameViewSet(viewsets.ModelViewSet):
    queryset = ChessGame.objects.all().order_by('-created_at')
    serializer_class = ChessGameSerializer

class MoveViewSet(viewsets.ModelViewSet):
    queryset = Move.objects.all()
    serializer_class = MoveSerializer
