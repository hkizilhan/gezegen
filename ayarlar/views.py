from django.shortcuts import render
from django import forms
from django.views import View

from . models import Ayar, AYAR_TURU
# Create your views here.



class GenelAyarlarForm(forms.Form):
    okul_adi = forms.CharField(label="Okul Adı", 
                        widget=forms.TextInput(attrs={'size': '80'}))
    
    
    


class AyarlarView(View):
    def get(self, request):
        
        form = GenelAyarlarForm()
        
        
        # OKUL_ADI
        try:
            ayar = Ayar.objects.get(ad='OKUL_ADI')
            form.fields["okul_adi"].initial = ayar.deger
        except Ayar.DoesNotExist:
            form.fields["okul_adi"].initial = 'Okul adı girilmemiş!'
            
        
        return render(request, 'ayarlar/ayarlar.html', {'form': form})
        
    
    def post(self, request):
        
        form = GenelAyarlarForm(request.POST)
        if form.is_valid():
            
            # OKUL_ADI
            okul_adi = Ayar.objects.get_or_create(ad='OKUL_ADI', 
                            bolum='genel', 
                            tur=AYAR_TURU.METIN, 
                            )[0]
            okul_adi.deger = form.cleaned_data['okul_adi']
            okul_adi.save()
            
                        
            
            # TODO: form kaydedildi mesajı görüntüle...
            
            return render(request, 'ayarlar/ayarlar.html', {'form': form})
        
        else:
            # TODO: Formda hata var mesajı görüntüle.
            
            return render(request, 'ayarlar/ayarlar.html', {'form': form})
        
