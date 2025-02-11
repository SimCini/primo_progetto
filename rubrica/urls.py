from django.contrib import admin
from django.urls import path, include
from .views import index, lista_contatti, dettagli_contatto


app_name="rubrica"

urlpatterns = [
    path('', index, name='index'),
    path('lista_contatti', lista_contatti, name='lista_contatti'),
    path('lista_contatti/<int:pk>', dettagli_contatto, name='dettagli_contatto'),

]
