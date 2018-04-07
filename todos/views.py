# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Todos
# Create your views here.
def index(request):
    todos = Todos.objects.all()[:10]
    context = {
        'name' : 'Mridul',
        'todos' : todos
    }
    return render(request, 'index.html', context)

def details(request, id):
    todos = Todos.objects.get(id=id)
    context = {
        'name' : 'Mridul',
        'todos' : todos
    }
    return render(request, 'details.html', context)
