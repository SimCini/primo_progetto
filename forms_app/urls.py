from django.urls import path
from forms_app.views import contatti, lista_contatti

app_name = "forms_app"
urlpatterns = [
    path('contattacci/', contatti, name='contatti'),
    path('contatti/', lista_contatti, name='lista_contatti'),
]