from .models import Filme

def novo(request):
    lista = Filme.objects.all().order_by("-data")[0:5]
    return {'filmes_novos':lista}

def popular(request):
    lista = Filme.objects.all().order_by('-visualizacao')[0:5]
    return {'filmes_populares':lista}
