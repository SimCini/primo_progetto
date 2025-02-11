from django.shortcuts import render, get_object_or_404
from django.db import models
from .models import Contatto

def index(request):
    return render(request, "index_rubrica.html")

def lista_contatti(request):
    contatti = Contatto.objects.all()

    context = {
                "contatti": contatti,
            }
    return render(request, "lista_contatti.html", context)

def dettagli_contatto(request):
    return render(request, "dettagli_contatto.html")

def dettagli_contatto(request, pk):
    contatto = get_object_or_404(Contatto, pk=pk)
    context = {
                "contatto": contatto
            }
    return render(request, "dettagli_contatto.html", context)