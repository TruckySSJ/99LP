from django.shortcuts import render
from .models import Project
from django.db.models import Count, Q
from django.shortcuts import render
from .models import Players

# Create your views here.

def portafolio(request):
    projects = Project.objects.all()
    return render(request,"portafolio/portafolio.html", {'projects':projects})  
   
  