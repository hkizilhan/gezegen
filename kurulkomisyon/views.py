from django.shortcuts import render
from django.views import View
from django import forms

from . apps import KurulKomisyonConfig as conf


class GenelAyarlarForm(forms.Form):
    antet = forms.CharField(label="Antet", 
                        widget=forms.Textarea(
                            attrs={'cols': '80', 'rows': '4'}
                            )
                        )
    kurumkodu = forms.CharField(label='Kurum Kodu')
    mudur     = forms.CharField(label='Okul Müdürü')
    baskan    = forms.CharField(label='Kurul Başkanı')
    uye1      = forms.CharField(label='1. Üye')
    uye2      = forms.CharField(label='2. Üye')
    okulaile  = forms.CharField(label='Okul Aile Bir. Bşk.')
    onur2bsk  = forms.CharField(label='Onur Kurulu 2. Bşk.')
    
    
    




class KurulIndexView(View):
    
    def get(self, request):
        form = GenelAyarlarForm()
        
        form.fields["antet"].initial     = conf.get('antet')
        form.fields["kurumkodu"].initial = conf.get('kurumkodu')
        form.fields["mudur"].initial     = conf.get('mudur')
        form.fields["baskan"].initial    = conf.get('baskan')
        form.fields["uye1"].initial      = conf.get('uye1')
        form.fields["uye2"].initial      = conf.get('uye2')
        form.fields["okulaile"].initial  = conf.get('okulaile')
        form.fields["onur2bsk"].initial  = conf.get('onur2bsk')
        
        
        return render(request, 'kurulkomisyon/disiplin_index.html', {'form': form})
        
        
    def post(self, request):
        form = GenelAyarlarForm(request.POST)
        
        if form.is_valid():
            conf.set('antet',     form.cleaned_data['antet'])
            conf.set('kurumkodu', form.cleaned_data['kurumkodu'])
            conf.set('mudur', form.cleaned_data['mudur'])
            conf.set('baskan', form.cleaned_data['baskan'])
            conf.set('uye1', form.cleaned_data['uye1'])
            conf.set('uye2', form.cleaned_data['uye2'])
            conf.set('okulaile', form.cleaned_data['okulaile'])
            conf.set('onur2bsk', form.cleaned_data['onur2bsk'])
            
            
            conf.save_config()
            
            # TODO: form kaydedildi mesajı görüntüle...
            return render(request, 'kurulkomisyon/disiplin_index.html', {'form': form})
            
        
        else:
            # TODO: Formda hata var mesajı görüntüle.
            
            return render(request, 'ayarlar/ayarlar.html', {'form': form})
        
        

