from django.db import models

# Create your models here.

class Ogrenci(models.Model):
    
    CINSIYET = (('Erkek', 'Erkek'), ('Kız', 'Kız'))
    
    
    no       = models.PositiveIntegerField(unique=True)
    sinif    = models.CharField(max_length=50, verbose_name= 'Sınıf')
    ad       = models.CharField(max_length=50)
    soyad    = models.CharField(max_length=50)
    cinsiyet = models.CharField(max_length=50, choices=CINSIYET)
    
    def __str__(self):
        return '{} - {}'.format(self.no, self.ad + " " + self.soyad)
        
    class Meta:
        ordering = ['sinif', 'no']
