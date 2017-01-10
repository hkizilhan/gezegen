from django.db import models

# Create your models here.

class Ustyazi(models.Model):
    dosya_no      = models.CharField(max_length=20)
    sayi_no       = models.CharField(max_length=20)
    tarih         = models.DateField()
    konu          = models.CharField(max_length=200)
    nereye        = models.CharField(max_length=200)
    ilgi          = models.CharField(max_length=200, blank=True)
    yazi          = models.CharField(max_length=200)
    ek            = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return '{} - {}'.format(self.sayi_no, self.konu)
        
    class Meta:
        default_permissions = ('ekle', 'güncelle', 'sil', 'görüntüle')
