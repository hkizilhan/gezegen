from django.db import models

# Create your models here.


class AYAR_TURU():
    METIN = 1
    SAYI  = 2
    BOOL  = 3
    
    


class Ayar(models.Model):
    BOLUM = (('genel', 'Genel Ayarlar'),)
    
    
    ad            = models.CharField(max_length=50, unique=True)
    bolum         = models.CharField(max_length=200, choices=BOLUM)
    tur           = models.CharField(max_length=200)
    deger         = models.CharField(max_length=200)
    
    
    def __str__(self):
        return '{}'.format(self.ad)
        
    class Meta:
        default_permissions = ('ekle', 'güncelle', 'sil', 'görüntüle')

