from django.urls import path
from .views import index, lista_corsi, lista_dettagli, dettagli_corso, view_a, view_c, view_d, view_e, view_f

app_name = "corsi_formazione"

urlpatterns = [
    path('', index, name='index'),
    path('lista_corsi', lista_corsi, name='lista_corsi'),
    path('lista_dettagli', lista_dettagli, name='lista_dettagli'),
    path('lista_dettagli/<int:pk>', dettagli_corso, name='dettagli_corso'), #view_b
    path('view_a', view_a, name='view_a'),
    path('view_c', view_c, name='view_c'),
    path('view_d', view_d, name='view_d'),
    path('view_e', view_e, name='view_e'),
    path('statistiche', view_f, name='statistiche'),
]