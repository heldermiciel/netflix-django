# Generated by Django 5.1.1 on 2024-09-30 17:05

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('thumb', models.ImageField(upload_to='thump_filme')),
                ('titulo', models.CharField(max_length=250)),
                ('descricao', models.TextField(max_length=2000)),
                ('categoria', models.CharField(choices=[('acao', 'acao'), ('comedia', 'comedia'), ('terror', 'terror'), ('ficcao', 'ficcao'), ('drama', 'drama')], max_length=15)),
                ('visualizacao', models.IntegerField(default=0)),
            ],
        ),
    ]
