"""nuevenuevelp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from core import views as core_views
from portafolio import views as portafolio_views
from django.conf.urls import url
from django.contrib import admin
#from django.conf.urls import include, url

from django.conf import settings

urlpatterns = [
    path('', core_views.home, name="home"),
    path('estadisticass/', core_views.estadisticas, name="estadisticass"),
    path('estadisticas/', core_views.graf_barras, name="estadisticas"),
    #path('estadisticas/', core_views.cant_adc, name="estadisticas"),
    path('portafolio/', portafolio_views.portafolio, name="portafolio"),
    path('tablaplayers/', core_views.tabla_players, name="tablaplayers"),
    path('admin/', admin.site.urls),
    #path('tablaplayers/', include('core.urls')),
   # url(r'^$',"core_views.tabla_players"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


