from rest_framework import viewsets

from destino.models import Destino
from destino.serializer import DestinoSerializer


class DestinosViewSet(viewsets.ModelViewSet):
    """Exibir todos os Destinos"""
    queryset = Destino.objects.all()
    serializer_class = DestinoSerializer