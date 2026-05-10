from django import forms
from .models import Cliente


class Form(forms.ModelForm):
    class Meta:
        model = Cliente

        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'campo-nome campo',
                'placeholder': 'Seu nome'}),

            'email': forms.EmailInput(attrs={
                'class': 'campo-email campo',
                'placeholder': 'exemplo@email.com'}),

            'mensagem': forms.Textarea(attrs={
                'class': 'campo-mensagem campo',
                'placeholder': 'Deixe aqui sua mensagem...',
                'maxlength': '1500'}),

            'telefone': forms.TextInput(attrs={
                'class': 'campo-telefone campo',
                'placeholder': '(00)00000-0000',}),

            'empresa': forms.TextInput(attrs={
                'class': 'campo-empresa campo',
                'placeholder': 'Nome da empresa'})
        }

        error_messages = {
            'mensagem': {
                'max_length': 'A mensagem deve ter no máximo 1500 caracteres.'
            }
        }


    def clean_mensagem(self):
        mensagem = self.cleaned_data.get('mensagem')
        if len(mensagem) > 1500:
            raise forms.ValidationError(
                'A mensagem deve ter no máximo 1500 caracteres.')
        return mensagem
