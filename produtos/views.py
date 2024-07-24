from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa


# Create your views here.
def ver_produto(request):
    if request.method == "GET":
        return render(request, "ver_produto.html", {"nome": "Alice"})
    elif request.method == "POST":
        nome = request.POST.get("nome")
        idade = request.POST.get("idade")

        pessoa = Pessoa(nome=nome, idade=idade)
        pessoa.save()
        return HttpResponse(f"Ola {nome}, sua idade é {idade} anos!")


def inserir_produto(request):
    return HttpResponse("Inserir produto")
