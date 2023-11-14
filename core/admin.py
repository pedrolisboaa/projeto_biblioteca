from django.contrib import admin
from .models import Assunto, Editora, Livro, Leitor, Emprestimo

# Register your models here.
@admin.register(Assunto)
class AssuntoAdmin(admin.ModelAdmin):
    list_display = 'assunto',
    ordering = 'assunto',

@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = 'id','nome', 'uf'
    ordering = 'id',
    
@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = 'id','titulo','disponivel', 'autor', 'editora', 'assunto', 'numero_paginas', 'dt_cadastramento' 
    ordering = 'id','disponivel'
    #list_editable = ('disponivel',)
    
    
@admin.register(Leitor)
class LeitorAdmin(admin.ModelAdmin):
    list_display = 'nome', 'sobrenome','cpf', 'email', 'telefone', 'sexo', 'dt_cadastramento',
    ordering = 'nome',


@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = 'livro', 'leitor', 'data_emprestimo', 'data_devolucao', 'finalizada'

