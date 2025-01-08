from django.urls import path
from .views import home, index, articoloDetailView, listaArticoli, queryBase, giornalistaDetailView

app_name = "news"

urlpatterns = [
    path('', index, name='index'),
    path('home', home, name='homeview'),
    path('articoli/<int:pk>', articoloDetailView, name='articolo_detail'),
    path('articoli', listaArticoli, name='lista_articoli'),
    path('giornalisti/<int:pk>', giornalistaDetailView, name='giornalista_detail'),
    #path('giornalisti', listaGiornalisti, name='lista_giornalisti'),
    path('query', queryBase, name='query_base')
]