from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from nivel0.models import Nivel0
from nivel0.serializers import Nivel0Serializer


class Nivel0CreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Nivel0.objects.all()
    serializer_class = Nivel0Serializer


class Nivel0RetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Nivel0.objects.all()
    serializer_class = Nivel0Serializer