
from .models import Player
from .serializers import PlayerSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class ListCreateView(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [IsAuthenticated]

class RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    model = Player
    permission_classes = [IsAuthenticated]