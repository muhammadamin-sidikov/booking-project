from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Game
from .serializers import GameSerializer, GameListSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameListSerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'create':
            return GameSerializer
        return GameListSerializer

