from django.contrib import admin
from core.models import Autor, Categoria, Leitor, Livro, Emprestimo

#Para a tabela do Model aparecer no /admin
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'criado', 'modificado', 'ativo')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'criado', 'modificado', 'ativo')

@admin.register(Leitor)
class LeitorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'email', 'status', 'criado', 'modificado', 'ativo')

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'categoria', 'autor', 'status', 'criado', 'modificado', 'ativo')

@admin.register(Emprestimo)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('leitor', 'livro', 'status', 'criado', 'modificado', 'ativo')