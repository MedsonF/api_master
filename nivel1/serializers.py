from rest_framework import serializers
from nivel1.models import Nivel1

class Nivel1Serializer(serializers.ModelSerializer):

    class Meta:
        model = Nivel1
        fields = '__all__'