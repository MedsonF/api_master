from rest_framework import serializers
from nivel2.models import Nivel2

class Nivel2Serializer(serializers.ModelSerializer):

    class Meta:
        model = Nivel2
        fields = '__all__'