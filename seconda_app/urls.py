from django.urls import path
from seconda_app.views import es_if, index, if_else_elif

app_name = "seconda_app"
urlpatterns = [
    path('es_if', es_if, name='es_if'),
    path('if_else_elif', if_else_elif, name='if_else_elif'),
    path('', index, name='index'),
]