from rest_framework import serializers
from categoria.models import PlanoFinanceiro
from nivel0.serializers import Nivel0Serializer
from nivel1.serializers import Nivel1Serializer
from nivel2.serializers import Nivel2Serializer
from nivel3.serializers import Nivel3Serializer
from nivel4.serializers import Nivel4Serializer
from nivel5.serializers import Nivel5Serializer


class PlanoFinanceiroSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlanoFinanceiro
        fields = '__all__'


class PlanoFinanceiroListDetailSerializer(serializers.ModelSerializer):
    nivel0 = Nivel0Serializer
    nivel1 = Nivel1Serializer
    nivel2 = Nivel2Serializer
    nivel3 = Nivel3Serializer
    nivel4 = Nivel4Serializer
    nivel5 = Nivel5Serializer

    class Meta:
        model = PlanoFinanceiro
        fields = ['id', 'codigo', 'plano_fin', 'nivel1', 'nivel2', 'nivel3', 'nivel4', 'nivel5']