from django.shortcuts import render
 

def index(request):
    return render(request, "visitante/index.html")

def sobre(request):
    return render(request, "sobre.html")