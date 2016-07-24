from django.conf.urls import url

from . import views

urlpatterns = [
    
    url(r'^$',                        views.Ustyazi_List.as_view(),     name='ustyazi-liste'),
    url(r'yeni$',                     views.Ustyazi_Create.as_view(),   name='ustyazi-yeni'),
    url(r'guncelle/(?P<pk>[0-9]+)$',  views.Ustyazi_Update.as_view(),   name='ustyazi-guncelle'),
    url(r'sil/(?P<pk>[0-9]+)$',       views.Ustyazi_Delete.as_view(),   name='ustyazi-sil'),
    
    url(r'odtrender/(?P<pk>[0-9]+)$', views.odtrender,                  name='ustyazi-render'),
    
    
    # ex: /polls/5/
    #url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    
]
