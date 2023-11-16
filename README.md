# Sistema de Biblioteca Simples

Este é um sistema de biblioteca simples desenvolvido como projeto de estudo. Ele foi construído utilizando HTML, CSS, JavaScript, Django, Bootstrap, AJAX e SQLite. O objetivo principal do sistema é permitir o cadastro de livros e autores, além de facilitar o processo de retirada e devolução de livros.

## Funcionalidades

1. **Cadastro de Livros e Autores:**
   - Permite adicionar novos livros, especificando título, autor e outras informações relevantes.
   - Oferece a possibilidade de cadastrar novos autores, incluindo detalhes como nome, nacionalidade, e data de nascimento.

2. **Retirada de Livros:**
   - Permite registrar a retirada de livros por parte dos usuários.
   - Inclui informações como o nome do usuário, data de retirada e prazo de devolução.

3. **Devolução de Livros:**
   - Facilita o processo de devolução, registrando a data em que o livro foi devolvido.

## Tecnologias Utilizadas

- **Front-end:**
  - HTML
  - CSS
  - JavaScript
  - Bootstrap 

- **Back-end:**
  - Django
  - SQLite

- **Interação Assíncrona:**
  - AJAX (para operações assíncronas, melhorando a eficiência e a experiência do usuário)

## Como Executar o Projeto

1. Certifique-se de ter o Python e o Django instalados em sua máquina.
2. Clone este repositório: `git clone https://github.com/seu-usuario/sistema-biblioteca.git`
3. Navegue até o diretório do projeto: `cd sistema-biblioteca`
4. Execute as migrações do banco de dados: `python manage.py migrate`
5. Inicie o servidor: `python manage.py runserver`
6. Acesse o sistema em seu navegador: `http://localhost:8000`

Lembre-se de que este sistema é básico e foi criado para fins educacionais. Fique à vontade para explorar, modificar e aprimorar conforme necessário para atender às suas necessidades de aprendizado.
