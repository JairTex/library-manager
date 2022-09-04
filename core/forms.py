from django import forms
from core.models import Autor, Categoria, Leitor, Livro, Emprestimo

class CategoriaModelForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']

class AutorModelForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome']


class LeitorModelForm(forms.ModelForm):
    class Meta:
        model = Leitor
        fields = ['nome', 'telefone', 'email']

class LivroModelForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['codigo', 'nome', 'categoria', 'autor']

class EmprestimoModelForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['leitor', 'livro']