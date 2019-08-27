from django.shortcuts import render, HttpResponse
#from portafolio.models import *
from django.shortcuts import render
#from django.db.models import Count, Q
from django.shortcuts import render
from portafolio.models import Players
from django.db import connection
#from django.db.models import Count
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request,"core/home.html")

def estadisticas(request):
    return render(request,"core/estadisticas.html")

  

def tablaplayers(request):
    return render(request,"core/tablaplayers.html")  

def graf_barras(request):
    all_players = Players.objects.all()
    cant_adc = Players.objects.filter(position='ADC').count()
    cant_supp = Players.objects.filter(position='SUPPORT').count()
    cant_mid = Players.objects.filter(position='MID').count()
    cant_jg = Players.objects.filter(position='JUNGLE').count()
    cant_top = Players.objects.filter(position='TOP').count()
    best_adc = Players.objects.filter(player='Hiro').filter(position='ADC')
    best_supp = Players.objects.filter(player='Cupcake').filter(position='SUPPORT')
    best_mid = Players.objects.filter(player='Yoshino').filter(position='MID')
    best_jg = Players.objects.filter(player='NikoleX').filter(position='JUNGLE')
    best_top = Players.objects.filter(player='Thien').filter(position='TOP')
    adc_kills = Players.objects.filter(position='ADC')
    adc_ficha = Players.objects.filter(win_rate='100%').filter(position='ADC').count()
    supp_ficha = Players.objects.filter(win_rate='100%').filter(position='SUPPORT').count()
    mid_ficha = Players.objects.filter(win_rate='100%').filter(position='MID').count()
    jg_ficha = Players.objects.filter(win_rate='100%').filter(position='JUNGLE').count()
    top_ficha = Players.objects.filter(win_rate='100%').filter(position='TOP').count()
    return render(request, 'core/estadisticas.html',{'cant_adc': cant_adc, 'cant_supp': cant_supp, 'cant_mid': cant_mid, 'cant_jg': cant_jg, 'cant_top': cant_top, 'all_players': all_players, 'best_adc': best_adc, 'best_supp': best_supp, 'best_mid': best_mid, 'best_jg': best_jg, 'best_top': best_top, 'adc_kills': adc_kills, 'adc_ficha': adc_ficha, 'supp_ficha': supp_ficha, 'mid_ficha': mid_ficha, 'jg_ficha': jg_ficha, 'top_ficha': top_ficha})

def tabla_players(request):
    playerlist = Players.objects.all()
    return render(request, 'core/tablaplayers.html', {'playerlist': playerlist})

#def cant_adc(request):
 #   cant_adc = Players.objects.filter(position='ADC').count()
  #  return render(request, 'core/estadisticas.html', {'cant_adc': cant_adc})




