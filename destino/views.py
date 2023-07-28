from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.response import Response

from destino.models import Destino
from destino.serializer import DestinoSerializer


class DestinosViewSet(viewsets.ModelViewSet):
    """Exibir todos os Destinos"""
    queryset = Destino.objects.all()
    serializer_class = DestinoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome']
    
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        if len(queryset) < 1:
            return Response({"mensagem": "Nenhum destino foi encontrado"})
        return Response(serializer.data)