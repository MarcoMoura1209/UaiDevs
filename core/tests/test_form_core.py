from django.test import TestCase
from core.forms import Form


class FormTest(TestCase):
    def test_formulario_com_dados_validos(self):
        '''Formulario com dados validos deve ser aceito'''

        dados = {
            'nome':'Homem Teste',
            'email':'homemteste@gmail.com',
            'mensagem':'Ola, gostaria de conversar com voces',
            'telefone':'11999999999',
            'empresa':'Empresa Teste',
        }
        form = Form(data=dados)
        self.assertTrue(form.is_valid())

    def test_form_com_campo_nome_vazio(self):
        '''Form deve apontar erro para campo nome vazio'''

        dados = {
            'nome':'',
            'email':'homemteste@gmail.com',
            'mensagem':'Ola, gostaria de conversar com voces',
            'telefone':'11999999999',
            'empresa':'Empresa Teste',
        }
        form = Form(data=dados)
        self.assertFalse(form.is_valid())
        self.assertIn('nome', form.errors)

    def test_form_com_campo_email_vazio(self):
        '''Form deve apontar erro para campo email vazio'''

        dados = {
            'nome':'Homem Teste',
            'email':'',
            'mensagem':'Ola, gostaria de conversar com voces',
            'telefone':'11999999999',
            'empresa':'Empresa Teste',
        }
        form = Form(data=dados)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_form_com_campo_mensagem_vazio(self):
        '''Form deve apontar erro para campo mensagem vazio'''

        dados = {
            'nome':'Homem Teste',
            'email':'homemteste@gmail.com',
            'mensagem':'',
            'telefone':'11999999999',
            'empresa':'Empresa Teste',
        }
        form = Form(data=dados)
        self.assertFalse(form.is_valid())
        self.assertIn('mensagem', form.errors)

    def test_form_com_campo_telefone_vazio(self):
        '''Form deve apontar erro para campo telefone vazio'''

        dados = {
            'nome':'Homem Teste',
            'email':'homemteste@gmail.com',
            'mensagem':'Ola, gostaria de conversar com voces',
            'telefone':'',
            'empresa':'Empresa Teste',
        }
        form = Form(data=dados)
        self.assertFalse(form.is_valid())
        self.assertIn('telefone', form.errors)

    def test_form_com_campo_empresa_vazio(self):
        '''Form deve apontar erro para campo empresa vazio'''

        dados = {
            'nome':'Homem Teste',
            'email':'homemteste@gmail.com',
            'mensagem':'Ola, gostaria de conversar com voces',
            'telefone':'11999999999',
            'empresa':'',
        }
        form = Form(data=dados)
        self.assertFalse(form.is_valid())
        self.assertIn('empresa', form.errors)

    def test_mensagem_invalida_com_mais_de_1500_caracteres(self):
        '''Mensagens acimas de 1500 caracteres devem ser rejeitados'''

        dados = {
            'nome':'Homem Teste',
            'email':'homemteste@gmail.com',
            'mensagem':'x' * 1501,
            'telefone':'11999999999',
            'empresa':'Empresa Teste',
        }
        form = Form(data=dados)
        self.assertFalse(form.is_valid())
        self.assertIn('mensagem', form.errors)

    def test_mensagem_com_exatamente_1500_caracteres(self):
        '''Mensagens com exatos 1500 caracteres devem ser aceitos'''

        dados = {
            'nome':'Homem Teste',
            'email':'homemteste@gmail.com',
            'mensagem':'x' * 1500,
            'telefone':'11999999999',
            'empresa':'Empresa Teste',
        }
        form = Form(data=dados)
        self.assertTrue(form.is_valid())
        self.assertNotIn('mensagem', form.errors)
