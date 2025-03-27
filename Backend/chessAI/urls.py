from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChessGameViewSet, MoveViewSet, AIMoveView

router = DefaultRouter()
router.register(r'games', ChessGameViewSet)
router.register(r'moves', MoveViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('games/start/', ChessGameViewSet.as_view({'post': 'start_game'}), name='start-game'),
    path('games/<int:pk>/update_status/', ChessGameViewSet.as_view({'patch': 'update_status'}), name='update-status'),
    path('ai/move/', AIMoveView.as_view(), name='ai-move'),
]
