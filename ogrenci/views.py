from django.shortcuts import render

from django.views.generic import View, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin

from django.core.urlresolvers import reverse_lazy


from django.contrib import messages
from django import forms
from django.db import transaction

import xlrd
# Create your views here.

from . models import Ogrenci


def get_siniflar():
    return list( Ogrenci.objects.order_by().values_list('sinif', flat=True).distinct() )


class ListeForm(forms.Form):
    file1 = forms.FileField(label='Öğrencl Listesi') # , help_text='Öğrencl Listesi')
    file2 = forms.FileField(label='Şube Sayıları')   # , help_text='Şube Sayıları')




class Ogrenci_index(View):
    def get(self, request):
        # <view logic>
        
        context = {'aaa': 'bbb'}
        return render(request, 'ogrenci/index.html', context)


##
####
###### Generic edit views

class Ogrenci_List(ListView):
    model = Ogrenci


class Ogrenci_Create(SuccessMessageMixin, CreateView):
    model = Ogrenci
    fields = ['no', 'sinif', 'ad', 'soyad', 'cinsiyet']
    # fields = '__all__'
    
    success_url = reverse_lazy('tum-ogrenciler')
    success_message = 'Başarıyla kaydedildi...'
    
    def get_context_data(self, **kwargs):
        context = super(Ogrenci_Create, self).get_context_data(**kwargs)
        
        context['siniflar'] = get_siniflar()
        return context
    
    

class Ogrenci_Update(SuccessMessageMixin, UpdateView):
    model = Ogrenci
    fields = ['no', 'sinif', 'ad', 'soyad', 'cinsiyet']
    success_url = reverse_lazy('tum-ogrenciler')
    success_message = 'Başarıyla kaydedildi...'


class Ogrenci_Delete(DeleteView):
    model = Ogrenci
    success_url = reverse_lazy('tum-ogrenciler')
    success_message = 'Öğrenci Silindi.'
    
    # for success_message messages
    def delete(self, request, *args, **kwargs):
	    resp = super().delete(request, *args, **kwargs)
	    messages.add_message(request, messages.SUCCESS, self.success_message)
	    return resp

###### Generic edit views
####
##





class Liste_guncelle(View):
    def get(self, request):
        
        form = ListeForm()
        
        context = {'form': form}
        return render(request, 'ogrenci/liste_guncelle.html', context)
        
    def post(self, request):
        
        form = ListeForm(request.POST, request.FILES)
        
                
        # process form
        if form.is_valid():
            file1 = request.FILES['file1']
            file2 = request.FILES['file2']
            
            book1 = xlrd.open_workbook(file_contents=file1.read())
            book2 = xlrd.open_workbook(file_contents=file2.read())
            
            sheet1 = book1.sheet_by_index(0)
            sheet2 = book2.sheet_by_index(0)
            
            first_cell1 = str( sheet1.cell_value(rowx=0, colx=0) )
            first_cell2 = str( sheet2.cell_value(rowx=0, colx=0) )
            
            
            ogrenci_listesi, sube_listesi = None, None
            
            if first_cell1 == 'S.No':
                ogrenci_listesi = sheet1
            elif first_cell1 == 'Sınıf/Şube (Alan)':
                sube_listesi = sheet1
            
            if first_cell2 == 'Sınıf/Şube (Alan)':
                sube_listesi = sheet2
            elif first_cell2 == 'S.No':
                ogrenci_listesi = sheet2
            
            
            if (ogrenci_listesi == None) or (sube_listesi == None):
                messages.error(request, 'Dosyalardan biri ya da ikisi tanınamadı')
                context = {'form': form}
                return render(request, 'ogrenci/liste_guncelle.html', context)
        
            else:
                messages.success(request, 'Dosyalar başarıyla tanımlandı.')
            
            # import data
            
            # get class names
            siniflar = list()
            row_counter = 0  
            while 1:
                row_counter += 1 # skip first row 'Sınıf/Şube (Alan)'
                cell_value = str( sube_listesi.cell_value(rowx=row_counter, colx=0) )
                if cell_value != '':
                    siniflar.append(cell_value)
                    continue
                else:
                    last_cell = str( sube_listesi.cell_value(rowx=row_counter, colx=7) )
                    if last_cell != '':
                        break
                        
                if row_counter > 200:
                    messages.error(request, 'Sınıf tarama sayısı aşıldı: row_count > 200')
        
                    context = {'form': form}
                    return render(request, 'ogrenci/liste_guncelle.html', context)
        
                        
            # siniflar başarıyla alındı.
            messages.info(request, siniflar)
            
            row_counter = 0    # excell dosyasındaki kayıt satırı
            list_counter = 0   # siniflar listesinin indisi
            
            yeni_ogr_listesi = list()
            
            while 1:
                row_counter += 1 # skip first row 'S.No'
                cell_value = str( ogrenci_listesi.cell_value(rowx=row_counter, colx=0) )
                
                if cell_value == '':
                    # listenin sonuna ulaşıldı
                    break
                
                elif cell_value[0] == 'K':
                    # sınıf sonuna ulaşıldı
                    list_counter += 1
                    continue
                
                else:
                    # kayıtları al
                    no    = int( ogrenci_listesi.cell_value(rowx=row_counter, colx=1) )
                    sinif = siniflar[list_counter]
                    ad    = str( ogrenci_listesi.cell_value(rowx=row_counter, colx=3) )
                    soyad = str( ogrenci_listesi.cell_value(rowx=row_counter, colx=8) )
                    cinsiyet = str( ogrenci_listesi.cell_value(rowx=row_counter, colx=13) )
                    
                    # print(no, sinif, ad, soyad, cinsiyet)
                    # verileri listeye al
                    yeni_ogr_listesi.append((no, sinif, ad, soyad, cinsiyet))
            
            # end while
            # ogrencileri kaydet
            with transaction.atomic():
                
                Ogrenci.objects.all().delete()
                
                for ogr in yeni_ogr_listesi:
                    o = Ogrenci()
                    o.no       = ogr[0]
                    o.sinif    = ogr[1]
                    o.ad       = ogr[2]
                    o.soyad    = ogr[3]
                    o.cinsiyet = ogr[4]
                    o.save()
                    
        
        
        # invalid form        
        else:
            messages.error(request, 'İki dosyayı da yüklemeniz gerek.')
        
        context = {'form': form}
        return render(request, 'ogrenci/liste_guncelle.html', context)
        
        
