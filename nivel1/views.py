from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from nivel1.models import Nivel1
from nivel1.serializers import Nivel1Serializer


class Nivel1CreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Nivel1.objects.all()
    serializer_class = Nivel1Serializer


class Nivel1RetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Nivel1.objects.all()
    serializer_class = Nivel1Serializer