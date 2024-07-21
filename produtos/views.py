from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def ver_produto(request):
    return HttpResponse("Ver produto")


def inserir_produto(request):
    return HttpResponse("Inserir produto")
