from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def agendamento(request):
    return render(request, 'agendamento.html')

def cadastro(request):
    return render(request, 'cadastro.html')