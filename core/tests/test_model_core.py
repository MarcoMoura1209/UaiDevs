from django.test import TestCase
from ..models import Cliente


class ClientModelTest(TestCase):

    def setUp(self):
        self.cliente = Cliente.objects.create(
            nome = 'Homem Teste',
            email = 'homemteste@gmail.com',
            mensagem = 'Ola, gostaria de poder estar conversando com voces!',
            telefone = '38999999999',
            empresa = 'Empresa Teste',
        )
        return super().setUp()

    def test_cliente_criado_com_sucesso(self):
        self.assertEqual(Cliente.objects.count(), 1)

    def test_nome_salvado_corretamente(self):
        self.assertEqual(self.cliente.nome, 'Homem Teste')

    def test_str_retorna_nome_do_cliente(self):
        self.assertEqual(str(self.cliente), 'Homem Teste')


    def test_nome_invalido_com_mais_de_30_caracteres(self):
        '''Nome nao pode ultrapassar mais de 30 caracteres'''

        cliente_invalido = Cliente(
            nome = 'x' * 31,
            email = 'homemteste@gmail.com',
            mensagem = 'Ola, gostaria de poder estar conversando com voces!',
            telefone = '38999999999',
            empresa = 'Empresa Teste',
        )
        with self.assertRaises(Exception):
            cliente_invalido.full_clean()
            cliente_invalido.save()

    def test_empresa_invalida_com_mais_de_30_caracteres(self):
        '''Nome da empresa nao pode ultrapassar mais de 30 caracteres'''

        cliente_invalido = Cliente(
            nome = 'Homem Teste',
            email = 'homemteste@gmail.com',
            mensagem = 'Ola, gostaria de poder estar conversando com voces!',
            telefone = '38999999999',
            empresa = 'x' * 31,
        )
        with self.assertRaises(Exception):
            cliente_invalido.full_clean()
            cliente_invalido.save()

    def test_mensagem_invalida_com_mais_de_1500_caracteres(self):
        '''Mensagem nao pode ultrapassar mais de 1500 caracteres'''

        cliente_invalido = Cliente(
            nome = 'Homem Teste',
            email = 'homemteste@gmail.com',
            mensagem = 'x' * 1501,
            telefone = '38999999999',
            empresa = 'Empresa Teste',
        )
        with self.assertRaises(Exception):
            cliente_invalido.full_clean()
            cliente_invalido.save()

    def test_telefone_invalido_com_numeros_insuficientes(self):
        '''Telefone com formato invalido deve ser rejeitado'''

        cliente_invalido = Cliente(
            nome = 'Homem Teste',
            email = 'homemteste@gmail.com',
            mensagem = 'Ola, gostaria de poder estar conversando com voces!',
            telefone = '123',
            empresa = 'Empresa Teste',
        )
        with self.assertRaises(Exception):
            cliente_invalido.full_clean()
            cliente_invalido.save()

    def test_telefone_valido_com_formato_correto(self):
        cliente_valido = Cliente(
            nome = 'Homem Teste',
            email = 'homemteste@gmail.com',
            mensagem = 'Ola, gostaria de poder estar conversando com voces!',
            telefone = '11999999999',
            empresa = 'Empresa Teste',
        )

        cliente_valido.full_clean()
        cliente_valido.clean()

    def test_email_invalido_sem_arroba (self):
        cliente_invalido = Cliente(
            nome = 'Homem Teste',
            email = 'email-sem-arroba-gmail.com',
            mensagem = 'Ola, gostaria de poder estar conversando com voces!',
            telefone = '11999999999',
            empresa = 'Empresa Teste',
        )
        with self.assertRaises(Exception):
            cliente_invalido.full_clean()
            cliente_invalido.save()

    def test_email_com_formato_valido(self):
        cliente_valido = Cliente(
            nome = 'Homem Teste',
            email = 'homemteste@gmail.com',
            mensagem = 'Ola, gostaria de poder estar conversando com voces!',
            telefone = '11999999999',
            empresa = 'Empresa Teste',
        )
        cliente_valido.full_clean()
        cliente_valido.clean()
