from django.urls import path
from news.views import home, index

app_name = "prima_app"
urlpatterns = [
    path('', index, name='index'),
    path('home', home, name='home'),
]