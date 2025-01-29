from django.shortcuts import render
from django.db import models
from .models import Evento
import datetime

def index(request):
    return render(request, "index_eventi.html")

def view_a(request):
    eventi_per_data = Evento.objects.order_by('data')

    context = {
        'eventi_per_data': eventi_per_data,
    }
    return render(request,'view_a.html',context)

def view_b(request):
    eventi = Evento.objects.all()

    context = {
        'eventi': eventi,
    }
    return render(request,'view_b.html',context)

def view_c(request):
    somma=0
    c=0
    eventi = Evento.objects.all()
    for evento in eventi:
        somma+=evento.partecipanti
        c+=1

    context = {
        'tot_partecipanti': somma,
        'media_partecipanti': somma/c,
    }
    return render(request,'view_c.html',context)

def view_d(request):
    max_p=0
    max_titolo=models.CharField(max_length=20)
    min_p=999
    min_titolo=models.CharField(max_length=20)

    eventi = Evento.objects.all()
    for evento in eventi:
        if evento.partecipanti>max_p:
            max_p=evento.partecipanti
            max_titolo=evento.titolo
        if evento.partecipanti<min_p:
            min_p=evento.partecipanti
            min_titolo=evento.titolo

    context = {
        'max_partecipanti': max_p,
        'min_partecipanti': min_p,
        'max_titolo':max_titolo,
        'min_titolo':min_titolo,
    }
    return render(request,'view_d.html',context)
