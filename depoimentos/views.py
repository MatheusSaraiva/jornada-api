from rest_framework import viewsets

from depoimentos.models import Depoimento
from depoimentos.serializer import DepoimentoSerializer


class DepoimentosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os depoimentos"""
    queryset = Depoimento.objects.all()
    serializer_class = DepoimentoSerializer