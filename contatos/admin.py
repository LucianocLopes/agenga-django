from re import search
from django.contrib import admin
from .models import Contato, Categoria


class ContatoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome_completo', 'nome', 'sobrenome', 'telefone', 'email', 'categoria', 'data_criacao', 'ativo']
    list_editable = ['telefone', 'email', 'ativo']
    list_display_links = ['nome_completo']
    search_fields = ('nome','sobrenome')
    # list_filter = ['nome', 'sobrenome']
    list_per_page = 10


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    list_display_links = ['nome']

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Contato, ContatoAdmin)
