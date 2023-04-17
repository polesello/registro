from django.shortcuts import render
from django.http import HttpResponse

from .models import Persona


def index(request):
    from random import randint
    totale_gatti = randint(0, 44)
    lista_gatti = range(totale_gatti)
    persone = Persona.objects.all()

    context = {
        'nome': 'Nello',
        'cognome': 'Polesello',
        'totale_gatti': totale_gatti,
        'lista_gatti': lista_gatti,
        'presenti': 6,
        'persone': persone,
    }

    print(context)
    return render(request, 'homepage.html', context)


def index_old(request):
    if 'one' in request.path:
        return HttpResponse("<h1 style='color:red'>Ciaone</h1>")
    else:
        return HttpResponse("<h4>Ciao</h4>")
    


def mostra_targa(request, targa):

    prossima = 'cc123aa'
    valid = targa[:2].isalpha() and targa[2:5].isdigit() and targa[5:].isalpha()
    square = False
    if len(targa) == 7 and valid:
        targa = targa.upper()

        prossima = targa[:2] + str(int(targa[2:5]) + 1).zfill(3) + targa[5:]

        targa = targa[:2] + ' &nbsp; ' + targa[2:]
        square = targa.startswith('Z')

    context = {
        'targa': targa,
        'valid': valid,
        'square': square,
        'prossima': prossima,
    }
    return render(request, 'targa.html', context)