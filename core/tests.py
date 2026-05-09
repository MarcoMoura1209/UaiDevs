from django.test import TestCase
from .models import Cliente


class ClientModelTest(TestCase):

    def setUp(self):
        self.cliente = Cliente.objects.create(
            nome = 'Homem Teste',
            email = 'homemteste@gmail.com',
            mensagem = 'Ola, gostaria de poder estar conversando com voces!',
            telefone = '+5538999999999',
            empresa = 'Empresa Teste',
        )
        return super().setUp()

    def test_cliente_criado_com_sucesso(self):
        self.assertEqual(Cliente.objects.count(), 1)
