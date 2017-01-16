from django.conf.urls import url

from . import views

urlpatterns = [
    
    url(r'^$', views.KurulIndexView.as_view(), name='kurul-index'),
    
    
]
