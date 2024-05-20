from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from nivel5.models import Nivel5
from nivel5.serializers import Nivel5Serializer


class Nivel5CreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Nivel5.objects.all()
    serializer_class = Nivel5Serializer


class Nivel5RetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Nivel5.objects.all()
    serializer_class = Nivel5Serializer