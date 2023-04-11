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
    return render(request, 'index.html', context)


def index_old(request):
    if 'one' in request.path:
        return HttpResponse("<h1 style='color:red'>Ciaone</h1>")
    else:
        return HttpResponse("<h4>Ciao</h4>")