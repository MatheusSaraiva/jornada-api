from rest_framework import viewsets

from depoimentos.models import Depoimento
from depoimentos.serializer import DepoimentoSerializer


class DepoimentosViewSet(viewsets.ModelViewSet):
    """Exibir todos os depoimentos"""
    queryset = Depoimento.objects.all()
    serializer_class = DepoimentoSerializer

class Depoimentos_homeViewSet(viewsets.ModelViewSet):
    """Exibir os depoimentos de 3 pessoas de forma randômica"""
    queryset = Depoimento.objects.all().order_by("?")[:3]
    serializer_class = DepoimentoSerializer
    http_method_names = ['get',]