from django.shortcuts import render, redirect
from .models import Livro, Leitor
from .form import LivroForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'index.html')


"""
    Livro
"""
def livro(request):
    livros = Livro.objects.order_by('-id')

    paginator = Paginator(livros, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {
        'livros': page_obj
    }
    
    return render(request, 'livro.html', context)


def buscar_livro(request):
    valor_buscar = request.GET.get('q', '').strip()
    if valor_buscar == '':
        return redirect('livro')
    
    livros = Livro.objects.filter(
        Q(titulo__icontains=valor_buscar) |
        Q(id__icontains=valor_buscar) |
        Q(autor__icontains=valor_buscar)).order_by('-id')
        
    paginator = Paginator(livros, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {
        'livros': page_obj
    }
    
    return render(request, 'livro.html', context)


def livro_adicionar(request):
    form = LivroForm()
    context = {
         'form': form
     }
    
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Livro cadastrado com sucesso.')
        else:
            messages.error(request, 'Erro ao cadastrar o Livro ')
        return redirect('livro_adicionar')
    return render(request, 'livro_adicionar.html', context)


def livro_atualizar(request, id_livro):
    livro = Livro.objects.get(pk=id_livro)

    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            messages.success(request, 'Alteração realizada com sucesso.')
    else:
        form = LivroForm(instance=livro)
        

    context  = {
        'livro': livro,
        'form': form,
    }

    return render(request, 'livro_atualizar.html', context)


def livro_deletar(request, id_livro):
    livro = Livro.objects.get(pk=id_livro)
    if request.method == 'POST':
        livro.delete()
        return redirect('livro')

    return render(request, 'livro_deletar.html', {'livro': livro})



# Leitor

def leitor(request):
    leitores = Leitor.objects.order_by('nome')
    
    paginator = Paginator(leitores, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {
        'leitores': page_obj
    }
    
    return render(request, 'leitor.html', context)


def buscar_leitor(request):
    valor_buscar = request.GET.get('q', '').strip()
    if valor_buscar == '':
        return redirect('leitor')
    leitores = Leitor.objects.filter(
        Q(nome__icontains=valor_buscar)|
        Q(sobrenome__icontains=valor_buscar)|
        Q(cpf__icontains=valor_buscar)|
        Q(email__icontains=valor_buscar)|
        Q(telefone__icontains=valor_buscar)
    ).order_by('-id')
    
    
    paginator = Paginator(leitores, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {
        'leitores': page_obj
    }
    
    return render(request, 'leitor.html', context)