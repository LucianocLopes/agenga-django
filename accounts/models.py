from pyexpat import model
from django.db import models
from django import forms
from contatos.models import Contato


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        exclude = ('ativo','data_criacao',)