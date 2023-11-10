from django.urls import path
from .views import index, livro, buscar_livro, livro_adicionar, livro_atualizar, livro_deletar

urlpatterns = [
    path('', index, name='index'),
    path('buscar/livro/', buscar_livro, name='buscar_livro'),
    #path('usuario/', usuario, name='usuario'),

    # CRUD de Livros
    path('livro/', livro, name='livro'),
    path('livro/adicionar/', livro_adicionar, name='livro_adicionar'),
    path('livro/atualizar/<int:id_livro>', livro_atualizar, name='livro_atualizar'),
    path('livro/deletar/<int:id_livro>', livro_deletar, name='livro_deletar'),
    
]