from django.contrib import admin
from django.contrib.admin import AdminSite
# Register your models here.

from .models import Ogretmen, Brans

admin.site.register([Ogretmen, Brans])


class OgretmenAdminSite(AdminSite):
    site_header = 'Öğretmen Bilgileri'

oretmen_admin_site = OgretmenAdminSite(name='ogretmen')
oretmen_admin_site.register([Ogretmen, Brans])
