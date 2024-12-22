from django.contrib import admin
from .models import Categoria, Receita, Comentario

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')

@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'usuario', 'categoria', 'data_criacao')
    list_filter = ('categoria', 'data_criacao')
    search_fields = ('titulo', 'descricao', 'ingredientes')

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('texto', 'usuario', 'receita', 'data_criacao')
    list_filter = ('data_criacao', 'receita')
    search_fields = ('texto',)
