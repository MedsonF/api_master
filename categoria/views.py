from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from categoria.models import PlanoFinanceiro
from categoria.serializers import PlanoFinanceiroSerializer, PlanoFinanceiroListDetailSerializer


class PlanoFinanceiroCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = PlanoFinanceiro.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PlanoFinanceiroListDetailSerializer
        return PlanoFinanceiroSerializer


class PlanoFinanceiroRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = PlanoFinanceiro.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PlanoFinanceiroListDetailSerializer
        return PlanoFinanceiroSerializer