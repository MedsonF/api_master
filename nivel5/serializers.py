from rest_framework import serializers
from nivel5.models import Nivel5

class Nivel5Serializer(serializers.ModelSerializer):

    class Meta:
        model = Nivel5
        fields = '__all__'