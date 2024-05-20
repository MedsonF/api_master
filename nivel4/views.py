from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from nivel4.models import Nivel4
from nivel4.serializers import Nivel4Serializer


class Nivel4CreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Nivel4.objects.all()
    serializer_class = Nivel4Serializer


class Nivel4RetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Nivel4.objects.all()
    serializer_class = Nivel4Serializer