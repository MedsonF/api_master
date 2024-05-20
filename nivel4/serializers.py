from rest_framework import serializers
from nivel4.models import Nivel4

class Nivel4Serializer(serializers.ModelSerializer):

    class Meta:
        model = Nivel4
        fields = '__all__'