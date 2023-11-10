import os
import sys
from pathlib import Path
import django
from django.conf import settings
from random import randint, choice

# Importar os modelos relevantes
from core.models import Editora, Assunto, Livro

# Configurar o ambiente Django
DJANGO_BASE_DIR = Path(__file__).parent.parent
sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
settings.USE_TZ = False

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

# Lista de nomes de editoras fictícias
editoras = [
    "Edições Aurora Boreal",
    "Editora Mar de Páginas",
    "Edições Sertão Literário",
    "Editora Ventos Alísios",
    "Edições Montanhas de Ideias",
    "Editora Rio de Emoções",
    "Edições Alquimia das Palavras",
    "Editora Lendas do Cerrado",
    "Edições Horizontes Mágicos",
    "Editora Encanto Amazônico",
    "Edições Sonhos Dourados",
    "Editora Pássaros do Pantanal",
    "Edições Flores do Nordeste",
    "Editora Lua Cheia",
    "Edições Palavras do Coração",
    "Editora Rios de Inspiração",
    "Edições Selva de Ideias",
    "Editora Céu Estrelado",
    "Edições Oásis das Letras",
    "Editora Aurora Boreal",
]


# Lista de títulos de livros fictícios, autores e número de páginas
livros = [
    {
        'titulo': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K. Rowling',
        'numero_paginas': 223,
    },
    {
        'titulo': 'O Senhor dos Anéis: A Sociedade do Anel',
        'autor': 'J.R.R. Tolkien',
        'numero_paginas': 423,
    },
    {
        'titulo': 'Cem Anos de Solidão',
        'autor': 'Gabriel García Márquez',
        'numero_paginas': 416,
    },
    {
        'titulo': 'Dom Quixote',
        'autor': 'Miguel de Cervantes',
        'numero_paginas': 863,
    },
    {
        'titulo': '1984',
        'autor': 'George Orwell',
        'numero_paginas': 328,
    },
    {
        'titulo': 'O Grande Gatsby',
        'autor': 'F. Scott Fitzgerald',
        'numero_paginas': 180,
    },
    {
        'titulo': 'Orgulho e Preconceito',
        'autor': 'Jane Austen',
        'numero_paginas': 308,
    },
    {
        'titulo': 'A Culpa é das Estrelas',
        'autor': 'John Green',
        'numero_paginas': 313,
    },
    {
        'titulo': 'A Revolução dos Bichos',
        'autor': 'George Orwell',
        'numero_paginas': 112,
    },
    {
        'titulo': 'Moby Dick',
        'autor': 'Herman Melville',
        'numero_paginas': 625,
    },
    {
        'titulo': 'O Pequeno Príncipe',
        'autor': 'Antoine de Saint-Exupéry',
        'numero_paginas': 96,
    },
    {
        'titulo': 'O Hobbit',
        'autor': 'J.R.R. Tolkien',
        'numero_paginas': 310,
    },
    {
        'titulo': 'Paraíso Perdido',
        'autor': 'John Milton',
        'numero_paginas': 348,
    },
    {
        'titulo': 'Anna Karenina',
        'autor': 'Leon Tolstói',
        'numero_paginas': 864,
    },
    {
        'titulo': 'Drácula',
        'autor': 'Bram Stoker',
        'numero_paginas': 488,
    },
    {
        'titulo': 'A Ilha do Tesouro',
        'autor': 'Robert Louis Stevenson',
        'numero_paginas': 217,
    },
    {
        'titulo': 'O Sol é para Todos',
        'autor': 'Harper Lee',
        'numero_paginas': 364,
    },
    {
        'titulo': 'As Vinhas da Ira',
        'autor': 'John Steinbeck',
        'numero_paginas': 464,
    },
    {
        'titulo': 'O Nome do Vento',
        'autor': 'Patrick Rothfuss',
        'numero_paginas': 662,
    },
    {
        'titulo': 'O Apanhador no Campo de Centeio',
        'autor': 'J.D. Salinger',
        'numero_paginas': 224,
    },
]


# Obter ou criar instâncias de editoras
for nome_editora in editoras:
    editora, created = Editora.objects.get_or_create(nome=nome_editora)

# Obter ou criar instâncias de assuntos
assunto, created = Assunto.objects.get_or_create(assunto="Ficção")
r
# Adicionar livros à base de dados
for livro_info in livros:
    livro = Livro(
        titulo=livro_info['titulo'],
        autor=livro_info['autor'],
        editora=choice(editoras),  # Seleciona uma editora aleatória
        assunto=assunto,  # Usando o mesmo assunto "Ficção" para todos os livros
        numero_paginas=livro_info['numero_paginas'],
    )
    livro.save()

print('Livros adicionados à base de dados')
