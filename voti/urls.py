from django.urls import path
from voti.views import index,lista_materie, lista_voti, media_voti, max_min

app_name = "voti"
urlpatterns = [
    path('index', index, name='index'),
    path('lista_materie', lista_materie, name='lista_materie'),
    path('lista_voti', lista_voti, name='lista_voti'),
    path('media_voti', media_voti, name='media_voti'),
    path('max_min_voti', max_min, name='max_min_voti'),

]