from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from destino.models import Destino


class DepoimentoApiTEST(APITestCase):
    
    def setUp(self):
        self.list_url = reverse('Destinos-list')
        self.destino_1 = Destino.objects.create(preco=540, nome='Belem', meta='meta1')
        self.destino_2 = Destino.objects.create(preco=780, nome='Santa Catarina', meta='meta2')

    def test_requisição_get_para_listar_destino(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_destino(self):
        data = {
            'preco': 154,
            'nome': 'Paraiba',
            'meta': 'meta'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_para_deletar_destino(self):
        response = self.client.delete('/destinos/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_requisicao_put_para_atualizar_destino(self):
        data = {
            'preco':150,
            'nome': "Belem",
            'meta': "meta1"
        }

        response = self.client.put('/destinos/1/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)