from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from nivel3.models import Nivel3
from nivel3.serializers import Nivel3Serializer


class Nivel3CreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Nivel3.objects.all()
    serializer_class = Nivel3Serializer


class Nivel3RetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Nivel3.objects.all()
    serializer_class = Nivel3Serializer