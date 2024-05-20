from rest_framework import serializers
from nivel3.models import Nivel3

class Nivel3Serializer(serializers.ModelSerializer):

    class Meta:
        model = Nivel3
        fields = '__all__'