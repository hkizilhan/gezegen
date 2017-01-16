from django.conf.urls import url

from . views import AyarlarView

urlpatterns = [
    url(r'^', AyarlarView.as_view(), name='ayarlar'),
]



