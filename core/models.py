from django.db import models


# Create your models here.
ESTADO_UF = [
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins')
]

SEXO = [
    ('M', 'Masculino'),
    ('F', 'Feminino'),
]


class Assunto(models.Model):
    assunto = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Assunto'
        verbose_name_plural = 'Assuntos'
    
    def save(self, *args, **kwargs):
        self.assunto = self.assunto.upper()
        super(Assunto, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.assunto


class Editora(models.Model):
    nome = models.CharField(max_length=150)
    uf = models.CharField(max_length=2, choices=ESTADO_UF)

    class Meta:
        verbose_name = 'Editora'
        verbose_name_plural = 'Editoras'
    
    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=250)
    autor = models.CharField(max_length=250)
    editora = models.ForeignKey(Editora, on_delete=models.SET_NULL, null=True)
    assunto = models.ForeignKey(Assunto, on_delete=models.SET_NULL, null=True)
    numero_paginas = models.IntegerField()
    disponivel = models.BooleanField(default=True)
    dt_cadastramento = models.DateField(auto_now_add=True)
    dt_ataulizacao = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
    

    def __str__(self):
        return self.titulo
    


class Leitor(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    sexo = models.CharField(max_length=1, choices=SEXO)
    dt_cadastramento = models.DateField(auto_now_add=True)
    dt_ataulizacao = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name ='Leitor'
        verbose_name_plural = 'Leitores'
        
    def __str__(self):
        return f'{self.nome} {self.sobrenome} - {self.cpf}'


class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    leitor = models.ForeignKey(Leitor, on_delete=models.CASCADE)
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField()

    def __str__(self):
        return f'{self.livro} emprestado para {self.leitor} - {self.leitor.cpf}'

    