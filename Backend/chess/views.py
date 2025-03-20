from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def handle_moves(request):
    move = request.data.get('move')
    return Response({'status': 'Move accpeted'})