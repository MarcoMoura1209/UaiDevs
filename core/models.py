from django.db import models
from django.core.exceptions import ValidationError
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    mensagem = models.TextField(max_length=1500, blank=False, null=False)
    telefone = PhoneNumberField(blank=False, null=False)
    empresa = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def clean(self):
        if len(self.mensagem) > 1500:
            raise ValidationError({
                'mensagem': 'A mensagem deve ter no máximo 1500 caracteres.'
            })

    def __str__(self):
        return self.nome
