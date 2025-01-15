from django.shortcuts import render

materie = ["Matematica","Italiano","Inglese","Storia","Geografia"]

voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],    
        'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
        'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}

def index(request):
    return render(request, "index_voti.html")

def lista_materie(request):
    context = {"materie": materie}
    return render(request, "lista_materie.html", context)

def lista_voti(request):
    context = {"voti": voti}
    return render(request, "lista_voti.html", context)

def media_voti(request):
    medie = []
    somma_voti=0
    for studente, voti_studente in voti.items():
        for materia, voto, assenze in voti_studente:
            somma_voti += voto
        numero_voti = len(voti_studente)
        media = somma_voti / numero_voti
        medie[studente] = media
    context = {"medie": medie}
    return render(request, "media_voti.html", context)

def max_min(request):
    voto_max = 0
    materie_max = []
    studenti_max = []
    voto_min = 0
    materie_min = []
    studenti_min = []

    for studente, voti_studenti in voti.items():
        for materia, voto, assenze in voti_studenti: 
            if (voto>voto_max):
                voto_max=voto
            if (voto<voto_min):
                voto_min=voto
    for studente, voti_studenti in voti.items():
        for materia, voto, assenze in voti_studenti: 
            if (voto==voto_max):
                if (not materia in materie_max):
                    materie_max.append(materia)
                if (not studente in studenti_max):
                    studenti_max.append(studente)
            if (voto==voto_min):
                if (not materia in materie_min):
                    materie_min.append(materia)
                if (not studente in studenti_max):
                    studenti_min.append(studente)            
                
    context = {
        "voto_max":voto_max,
        "voto_min":voto_min,
        "materie_max":materie_max,
        "materie_min":materie_min,
        "studenti_max":studenti_max,
        "studenti_min":studenti_min,
    }
    return render(request, "max_min_voti.html", context)