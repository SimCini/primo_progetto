"""
URL configuration for primo_progetto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from primo_progetto.views import index_root


app_name="primo_progetto"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prima_app/',include("prima_app.urls",namespace="prima_app")),
    path('seconda_app/',include("seconda_app.urls",namespace="seconda_app")),
    path('news/',include("news.urls",namespace="news")),
    path('voti/',include("voti.urls",namespace="voti")),
    path('eventi/',include("eventi.urls",namespace="eventi")),
    path('rubrica/',include("rubrica.urls",namespace="rubrica")),
    path('corsi_formazione/',include("corsi_formazione.urls",namespace="corsi_formazione")),
    path('', index_root, name='index_root'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('forms_app/',include("forms_app.urls",namespace="forms_app")),
    path('api/',include("api.urls",namespace="api")),
    path('products/',include("products.urls",namespace="products")),
]
