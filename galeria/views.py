from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>ALURA SPACE</h1>' \
    '<p>Seja bem vindo ao Espaço!</p>')


