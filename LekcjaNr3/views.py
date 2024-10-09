import random

from django.shortcuts import render

from .models import NaszPierwszyModel

def index(request):
    lista = NaszPierwszyModel.objects.all()

    return render(request, 'index.html', context={
        "elementy": lista
    })