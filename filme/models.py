from django.db import models
from django.utils import timezone

# Create your models here.

CATEGORIAS = (
    ('acao', 'acao'),
    ('comedia', 'comedia'),
    ('terror', 'terror'),
    ('ficcao', 'ficcao'),
    ('drama', 'drama')
)


class Filme(models.Model):
    data = models.DateTimeField(default=timezone.now)
    thumb = models.ImageField(upload_to='midia/thump_filme')
    titulo = models.CharField(max_length=250)
    descricao = models.TextField(max_length=2000)
    categoria = models.CharField(max_length=15, choices=CATEGORIAS)
    visualizacao = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo


class Episodio(models.Model):
    filme = models.ForeignKey('Filme', related_name="episodio", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=500)
    link = models.URLField()

    def __str__(self):
        return self.titulo
