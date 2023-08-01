from rest_framework import serializers

from destino.models import Destino


class DestinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destino
        fields = '__all__' 
