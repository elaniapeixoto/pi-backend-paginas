from django.shortcuts import render


def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")

def menu(request):
    return render(request, "menu.html")

