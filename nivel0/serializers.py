from rest_framework import serializers
from nivel0.models import Nivel0

class Nivel0Serializer(serializers.ModelSerializer):

    class Meta:
        model = Nivel0
        fields = '__all__'