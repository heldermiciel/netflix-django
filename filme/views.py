from django.shortcuts import render
from .models import Filme
from django.views.generic import ListView, DetailView, TemplateView


class Homepage(TemplateView):
    template_name = "home.html"


class Homefilmes(ListView):
    template_name = "homefilmes.html"
    model = Filme


class Detalhes(DetailView):
    template_name = "detalhe.html"
    model = Filme

    def get(self, request, *args, **kwargs):
        filme = self.get_object()
        filme.visualizacao += 1
        filme.save()
        return super().get(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        relacionado = Filme.objects.filter(categoria=self.get_object().categoria)
        context["relacionado"] = relacionado
        return context


class Pesquisa(ListView):
    template_name = 'pesquisa.html'
    model = Filme

    def get_queryset(self):
        termo = self.request.GET.get('query')
        if termo:
            object_list = Filme.objects.filter(titulo__icontains=termo)
            return object_list
        else:
            return None
