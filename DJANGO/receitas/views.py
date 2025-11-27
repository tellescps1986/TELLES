from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "home.html", 
    context={
                'nome':'Receitas Django'
    }) 


def sobre(request):
    return HttpResponse("sobre.html")

def receita(request):
    return HttpResponse("receita.html")
