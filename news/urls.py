from django.urls import path
from .views import home, index, articoloDetailView, listaArticoli

app_name = "news"

urlpatterns = [
    path('', index, name='index'),
    path('home', home, name='homeview'),
    path('articoli/<int:pk>', articoloDetailView, name='articolo_detail'),
    path('articoli', listaArticoli, name='lista_articoli'),
]