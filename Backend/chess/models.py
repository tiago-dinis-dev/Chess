from django.db import models

class ChessGame(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'In Progress'),
        ('checkmate', 'Checkmate'),
        ('stalemate', 'Stalemate'),
        ('draw', 'Draw'),
    ]

    game_id = models.AutoField(primary_key=True)
    player_white = models.CharField(max_length=100)
    player_black = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Move(models.Model):
    game = models.ForeignKey(ChessGame, on_delete=models.CASCADE, related_name='moves')
    move_number = models.IntegerField()
    move_notation = models.CharField(max_length=10)  # e.g., "e4", "Nf3", "O-O"
    created_at = models.DateTimeField(auto_now_add=True)
