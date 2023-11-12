from django import forms 
from .models import Livro, Leitor
from .models import Leitor


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ('titulo', 'autor', 'editora', 'assunto', 'numero_paginas')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'editora': forms.Select(attrs={'class': 'form-select'}),
            'assunto': forms.Select(attrs={'class': 'form-select'}),
            'numero_paginas': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class LeitorForm(forms.ModelForm):
    class Meta:
        model = Leitor
        fields = ('nome', 'sobrenome', 'cpf', 'email', 'telefone', 'sexo')
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'sobrenome': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-select'}),
            'email': forms.EmailInput(attrs={'class': 'form-select'}),
            'telefone': forms.NumberInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
        }
    
    # Configurando os erros do formulário
    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        leitor_id = self.instance.id if self.instance else None  # Obtém o ID do leitor se existir
        if Leitor.objects.exclude(id=leitor_id).filter(cpf=cpf).exists():
            self.add_error(
                'cpf',
                forms.ValidationError(
                    'CPF já cadastrado'
                )
            )
        return cpf
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        leitor_id = self.instance.id if self.instance else None  # Obtém o ID do leitor se existir
        if Leitor.objects.exclude(id=leitor_id).filter(email=email).exists():
            self.add_error(
                'email',
                forms.ValidationError(
                    'E-mail já cadastrado'
                )
            )
        return email
        
       