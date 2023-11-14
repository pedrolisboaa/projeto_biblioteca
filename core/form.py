from django import forms 
from .models import Livro, Leitor, Emprestimo
from dal import autocomplete


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
        
# class EmprestimoForm(forms.ModelForm):
    
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Filtando por livro 
#         self.fields['livro'].queryset = Livro.objects.filter(disponivel=True)
#         self.fields['leitor'].queryset = Leitor.objects.all()
    
#     class Meta:
#         model = Emprestimo
#         fields = ('livro', 'leitor', 'data_emprestimo', 'data_devolucao')     
#         widgets = {
#             'livro': forms.Select(attrs={'class': 'form-control'}),
#             'leitor': forms.Select(attrs={'class': 'form-control'}),
#             'data_emprestimo': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
#             'data_devolucao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
#         }


class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ('livro', 'leitor', 'data_emprestimo', 'data_devolucao')     
        widgets = {
            'livro':  autocomplete.ModelSelect2(url='livro-autocomplete', attrs={'class': 'form-control'}),
            'leitor': autocomplete.ModelSelect2(url='leitor-autocomplete', attrs={'class': 'form-control'}),
            'data_emprestimo': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'data_devolucao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        
        def clean(self):
            cleaned_data = super().clean()
            livro = cleaned_data.get('livro')

            # Verifique se o livro está disponível
            if livro and not livro.disponivel:
                raise forms.ValidationError('Este livro não está disponível para empréstimo.')

    
