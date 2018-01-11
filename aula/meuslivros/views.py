# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from meuslivros.models import Colecao

# Create your views here.

def home(request):
    return render(request, 'meuslivros/index.html')

#criando lista
def lista (request):
    lista = Colecao.objects.all()
    return render(request,'meuslivros/lista.html', {'lista' : lista})


