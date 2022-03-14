from distutils.command.upload import upload
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class Categoria(models.Model):
    nome = models.CharField(
        _('nome'),
        max_length=50,
    )

    def __str__(self) -> str:
        return self.nome
    

class Contato(models.Model):
    nome = models.CharField(
        _('nome'),
        max_length=50,
    )
    sobrenome = models.CharField(
        _('sobrenome'),
        max_length=100,
        null=True,
        blank=True,
    )
    telefone = models.CharField(
        _('telefone'),
        max_length=25,
    )
    email = models.EmailField(
        _('email'),
        null=True,
        blank=True,
    )
    data_criacao = models.DateTimeField(
        _('data de criação'),
        default=timezone.now,
    )
    biografia = models.TextField(
        verbose_name=_('biografia'),
        blank=True,
        null=True,
    )
    ativo = models.BooleanField(
        verbose_name=_('ativo'),
        default=True,
    )
    foto = models.ImageField(
        verbose_name=_('foto'),
        upload_to='fotos/%Y/%m/%d',
        blank=True,
        null=True,
    )
    categoria = models.ForeignKey(
        'Categoria',
        verbose_name=_('categoria'),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )


    class Meta:
        verbose_name = _('contato')
        verbose_name_plural = _('contatos')


    def __str__(self) -> str:
        return self.nome_completo
    

    def __repr__(self) -> str:
        return self.nome.strip().title()
    

    @property
    def nome_completo(self) -> str:
        return f'{self.nome.strip().title()} {self.sobrenome.strip().title()}'
    