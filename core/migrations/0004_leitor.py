# Generated by Django 4.2.7 on 2023-11-10 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_livro_dt_ataulizacao_alter_livro_dt_cadastramento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sobrenome', models.CharField(max_length=100)),
                ('cpf', models.IntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefone', models.CharField(max_length=20)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1)),
                ('dt_cadastramento', models.DateField(auto_now_add=True)),
                ('dt_ataulizacao', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Leitor',
                'verbose_name_plural': 'Leitores',
            },
        ),
    ]
