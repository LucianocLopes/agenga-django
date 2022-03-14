# Generated by Django 4.0.3 on 2022-03-12 22:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='nome')),
            ],
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='nome')),
                ('sobrenome', models.CharField(blank=True, max_length=100, null=True, verbose_name='sobrenome')),
                ('telefone', models.CharField(max_length=10, verbose_name='telefone')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email')),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now, verbose_name='data de criação')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contatos.categoria', verbose_name='categoria')),
            ],
            options={
                'verbose_name': 'contato',
                'verbose_name_plural': 'contatos',
            },
        ),
    ]
