from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request,"core/home.html")

def estadisticas(request):
    return render(request,"core/estadisticas.html")

def portafolio(request):
    return render(request,"core/portafolio.html")   

def tablaplayers(request):
    return render(request,"core/tablaplayers.html")  