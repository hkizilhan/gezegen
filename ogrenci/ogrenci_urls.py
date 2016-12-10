from django.conf.urls import url

from . import views

urlpatterns = [
    
    url(r'^$', views.Ogrenci_index.as_view(), name='ogrenci-index'),
    
    url(r'tum-ogrenciler$',          views.Ogrenci_List.as_view(),   name='tum-ogrenciler'),
    url(r'yeni$',                    views.Ogrenci_Create.as_view(), name='ogrenci-yeni'),
    url(r'guncelle/(?P<pk>[0-9]+)$', views.Ogrenci_Update.as_view(), name='ogrenci-guncelle'),
    url(r'sil/(?P<pk>[0-9]+)$',      views.Ogrenci_Delete.as_view(), name='ogrenci-sil'),
    
    url(r'liste-guncelle$', views.Liste_guncelle.as_view(), name='liste-guncelle'), 
    
    # ex: /polls/5/
    #url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    
]
