from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from depoimentos.models import Depoimento


class DepoimentoApiTEST(APITestCase):
    
    def setUp(self):
        self.list_url = reverse('Depoimentos-list')
        self.depoimento_1 = Depoimento.objects.create(depoimento='gostei muito', nome='lais balinha')
        self.depoimento_2 = Depoimento.objects.create(depoimento='não gostei', nome='Tatiana figueredo')

    def test_requisição_get_para_listar_depoimentos_home(self):
        url = reverse('Depoimentos_home-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisição_get_para_listar_depoimentos(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_depoimento(self):
        data = {
            'depoimento': 'depoimento teste',
            'nome': 'marta'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_para_deletar_depoimento(self):
        response = self.client.delete('/depoimentos/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_requisicao_put_para_atualizar_depoimento(self):
        data = {
            'depoimento':"estou comprando",
            'nome': "lais balinha"
        }

        response = self.client.put('/depoimentos/1/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)