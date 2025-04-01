from django.urls import path
from forms_app.views import contatti, lista_contatti, modifica_contatto, elimina_contatto

app_name = "forms_app"
urlpatterns = [
    path('contattacci/', contatti, name='contatti'),
    path('contatti/', lista_contatti, name='lista-contatti'),
    path('modifica_contatto/<int:pk>/', modifica_contatto, name='modifica-contatto'),
    path('elimina_contatto/<int:pk>/', elimina_contatto, name='elimina-contatto'),
]