from rest_framework import serializers
from .models import ChessGame, Move

class MoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Move
        fields = '__all__'

class ChessGameSerializer(serializers.ModelSerializer):
    moves = MoveSerializer(many=True, read_only=True)

    class Meta:
        model = ChessGame
        fields = '__all__'
