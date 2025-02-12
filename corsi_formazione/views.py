import datetime
from django.shortcuts import render, get_object_or_404
from .models import Corso

def index(request):
    return render(request, "index_corsi.html")

def lista_corsi(request):
    corsi = Corso.objects.all()

    context = {
                "corsi": corsi,
            }
    return render(request, "lista_corsi.html", context)

def lista_dettagli(request):
    corsi = Corso.objects.all()

    context = {
                "corsi": corsi,
            }
    return render(request, "lista_dettagli.html", context)

def dettagli_corso(request, pk): #view_b
    corso = get_object_or_404(Corso, pk=pk)
    context = {
                "corso": corso,
            }
    return render(request, "dettagli_corso.html", context)

def view_a(request):
    #elenco ordinato per data dei corsi
    corsi_ordinati = Corso.objects.order_by('data_inizio')
    context = {
                "corsi_ordinati": corsi_ordinati,
            }
    return render(request, "c_view_a.html", context)

#view_b fatta precedentemente con il nome dettagli_corso

def view_c(request):
    #corsi che iniziano dopo il 01/05/2025
    corsi_data = Corso.objects.filter(data_inizio__gt=datetime.date(2025,5,1))
    context = {
                "corsi_data": corsi_data,
            }
    return render(request, "c_view_c.html", context)

def view_d(request):
    #corsi con meno o uguale di 20 posti disponibili
    corsi_con_meno_20p = Corso.objects.filter(posti_disponibili__lte=20)
    context = {
                "corsi_con_meno_20p": corsi_con_meno_20p,
            }
    return render(request, "c_view_d.html", context)

def view_e(request):
    #corsi che terminano il 30/04/2025
    corsi_terminanti_giorno = Corso.objects.filter(data_fine=datetime.date(2025,4,30))
    context = {
                "corsi_terminanti_giorno": corsi_terminanti_giorno,
            }
    return render(request, "c_view_e.html", context)

def view_f(request):
    #statistiche avanzate
    corso_posti_maggiori = Corso.objects.order_by('-posti_disponibili').first()
    corso_posti_minori = Corso.objects.order_by('posti_disponibili').first()
    
    totale_posti=0
    corsi = Corso.objects.all()
    for corso in corsi:
        totale_posti+=corso.posti_disponibili

    context = {
                "corso_posti_maggiori": corso_posti_maggiori,
                "corso_posti_minori": corso_posti_minori,
                "totale_posti": totale_posti,
            }
    return render(request, "statistiche.html", context)