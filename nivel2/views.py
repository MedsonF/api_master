from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from nivel2.models import Nivel2
from nivel2.serializers import Nivel2Serializer


class Nivel2CreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Nivel2.objects.all()
    serializer_class = Nivel2Serializer


class Nivel2RetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Nivel2.objects.all()
    serializer_class = Nivel2Serializer