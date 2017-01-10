from django.db import models

# Create your models here.


class Brans(models.Model):
    
    ad       = models.CharField(max_length=50)
    kısaltma = models.CharField(max_length=50)
    
    def __str__(self):
        return '{} - {}'.format(self.ad, self.kısaltma)
        
    class Meta:
        ordering = ['ad', 'kısaltma']
        verbose_name = "Branş"
        verbose_name_plural = "Branşlar"



class Ogretmen(models.Model):
    
    KADROLU    = 'KADROLU'
    SOZLESMELI = 'SOZLESMELI'
    UCRETLI    = 'UCRETLI'
    
    OGRETMEN_ISTIHDAM_CHOICES = (
        (KADROLU,    'Kadrolu'),
        (SOZLESMELI, 'Sözleşmeli'),
        (UCRETLI,    'Ücretli'),
    )
    
    ad       = models.CharField(max_length=50)
    soyad    = models.CharField(max_length=50)
    brans    = models.ForeignKey(Brans, on_delete=models.PROTECT)
    tcno     = models.CharField(max_length=11, blank=True)
    istihdam = models.CharField(
        max_length=20,
        choices=OGRETMEN_ISTIHDAM_CHOICES,
        default=KADROLU,
    )
    telefon  = models.CharField(max_length=50, blank=True)
    eposta   = models.CharField(max_length=50, blank=True)
    
    
    def __str__(self):
        return '{} {} - {}'.format(self.ad, self.soyad, self.brans.kısaltma)
        
    class Meta:
        ordering = ['ad', 'soyad']
        verbose_name = "Öğretmen"
        verbose_name_plural = "Öğretmenler"

