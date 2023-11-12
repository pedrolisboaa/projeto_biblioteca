from django.urls import path
from .views import index, livro, buscar_livro, livro_adicionar, livro_atualizar, livro_deletar
from .views import leitor, buscar_leitor, leitor_adicionar, leitor_atualizar, leitor_deletar


urlpatterns = [
    path('', index, name='index'),
    
    # Buscadores 
    path('buscar/livro/', buscar_livro, name='buscar_livro'),
    path('buscar/leitor', buscar_leitor, name='buscar_leitor'),
    

    # CRUD de Livros
    path('livro/', livro, name='livro'),
    path('livro/adicionar/', livro_adicionar, name='livro_adicionar'),
    path('livro/atualizar/<int:id_livro>', livro_atualizar, name='livro_atualizar'),
    path('livro/deletar/<int:id_livro>', livro_deletar, name='livro_deletar'),
    
    # CRUD de Leitores
    path('leitor/', leitor, name='leitor'),
    path('leitor/adicionar/', leitor_adicionar, name='leitor_adicionar'),
    path('leitor/atualizar/<int:id_leitor>', leitor_atualizar, name='leitor_atualizar'),
    path('leitor/deletar/<int:id_leitor>', leitor_deletar, name='leitor_deletar'),
]