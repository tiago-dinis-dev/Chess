from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChessGameViewSet, MoveViewSet

router = DefaultRouter()
router.register(r'games', ChessGameViewSet)
router.register(r'moves', MoveViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('games/start/', ChessGameViewSet.as_view({'post': 'start_game'})),
    path('games/<int:pk>/update_status/', ChessGameViewSet.as_view({'patch': 'update_status'})),
]
