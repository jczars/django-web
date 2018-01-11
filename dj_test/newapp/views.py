# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from newapp.models import Post
from newapp.forms import PostForm

# Create your views here.
def home (request):
    var = 'testando a variável'
    return render(request,'newapp/index.html', {'var' : var})

#criando lista
def lista (request):
    lista = Post.objects.all().order_by('-id')
    return render(request,'newapp/lista.html', {'lista_posts' : lista})

def novo(request):
    form = PostForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(lista)

    return render(request, 'newapp/novo.html', {'form': form})


def atualiza(request, id):
    post = Post.objects.get(id=id)
    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return redirect(lista)

    return render(request, 'newapp/novo.html', {'form': form})

def deletar(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect(lista)

