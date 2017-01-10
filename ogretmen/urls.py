from django.conf.urls import url

from ogretmen.admin import oretmen_admin_site

urlpatterns = [
    url(r'^admin', oretmen_admin_site.urls),
]



