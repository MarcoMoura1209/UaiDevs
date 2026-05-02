from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    mensagem = models.TextField(blank=False, null=False)
    telefone = PhoneNumberField(region="BR", blank=False, null=False)
    empresa = models.CharField(max_length=30)

    class Meta: 
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


    def __str__(self):
        return self.nome
