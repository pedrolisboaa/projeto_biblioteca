from django.contrib import admin
from .models import Assunto, Editora, Livro, Leitor

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
    list_display = 'id','titulo', 'autor', 'editora', 'assunto', 'numero_paginas', 'dt_cadastramento' 
    ordering = 'id',
    
@admin.register(Leitor)
class LeitorAdmin(admin.ModelAdmin):
    list_display = 'nome', 'sobrenome','cpf', 'email', 'telefone', 'sexo', 'dt_cadastramento',
    ordering = 'nome',


