from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def ver_produto(request):
    return render(request, "ver_produto.html", {"nome": "Alice"})


def inserir_produto(request):
    return HttpResponse("Inserir produto")
