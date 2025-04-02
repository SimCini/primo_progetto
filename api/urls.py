from django.urls import path
from .views import todos_view, test_spotify

app_name = "api"
urlpatterns = [
    path('todos/', todos_view, name='todos'),
    path('spotify/', test_spotify, name='spotify')
]
