from django.urls import path
from .views import Homepage, Homefilmes, Detalhes, Pesquisa

app_name = 'filme'

urlpatterns = [
    path('', Homepage.as_view(), name='home'),
    path('filmes', Homefilmes.as_view(), name='homefilmes'),
    path('detalhe/<int:pk>', Detalhes.as_view(), name='detalhes'),
    path('pesquisa/', Pesquisa.as_view(), name='pesquisa')
]
