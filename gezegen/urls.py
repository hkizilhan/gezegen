"""gezegen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url

from django.contrib import admin
from django.views.generic.base import TemplateView
from django.contrib.auth.views import login, logout

from home.views import index

urlpatterns = [
    url(r'^$', index, name='home'),
    
    url(r'^ayarlar/', include('ayarlar.urls')),
    url(r'^ustyazi/', include('ustyazi.ustyazi_urls')),
    url(r'^ogrenci/', include('ogrenci.ogrenci_urls')),
    url(r'^ogretmen/', include('ogretmen.urls')),
    url(r'^kurulkomisyon/', include('kurulkomisyon.urls')),
    
    
    
    url(r'^admin/', admin.site.urls),
    
    url(r'^giris', login, {'template_name': 'admin/login.html'}),
    url(r'^cikis/$', logout, {'template_name': 'home/base.html'}),
    
    #url('^', include('django.contrib.auth.urls')),
]
