from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
# permission_required = ('polls.can_open', 'polls.can_edit')


from secretary import Renderer

from .models import Ustyazi


def index(request):
    context = {'aaa': 'bbb'}
    return render(request, 'ustyazi/index.html', context)


class Ustyazi_List(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Ustyazi
    permission_required = 'ustyazi.görüntüle_ustyazi'
    

class Ustyazi_Create_Form(forms.ModelForm):
    class Meta:
        model = Ustyazi
        fields = ['dosya_no', 'sayi_no', 'tarih', 'konu', 'nereye', 'ilgi', 'yazi', 'ek']
        widgets = {
            'yazi': forms.Textarea()
        }

class Ustyazi_Create(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Ustyazi
    permission_required = 'ustyazi.ekle_ustyazi'
    form_class = Ustyazi_Create_Form
    #fields = ['dosya_no', 'sayi_no', 'tarih', 'konu', 'nereye', 'ilgi', 'yazi', 'ek']
    success_url = reverse_lazy('ustyazi-liste')
    success_message = 'Başarıyla kaydedildi...'
    
    
class Ustyazi_Update(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Ustyazi
    permission_required = 'ustyazi.güncelle_ustyazi'
    form_class = Ustyazi_Create_Form
    #fields = ['dosya_no', 'sayi_no', 'tarih', 'konu', 'nereye', 'ilgi', 'yazi', 'ek']
    success_url = reverse_lazy('ustyazi-liste')
    success_message = 'Başarıyla kaydedildi...'


class Ustyazi_Delete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Ustyazi
    permission_required = 'ustyazi.sil_ustyazi'
    success_url = reverse_lazy('ustyazi-liste')
    success_message = 'Üstyazı Silindi.'
    
    def delete(self, request, *args, **kwargs):
	    resp = super().delete(request, *args, **kwargs)
	    messages.add_message(request, messages.INFO, self.success_message)
	    return resp


def odtrender(request, pk):
	# Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/vnd.oasis.opendocument.text ')
    response['Content-Disposition'] = 'attachment; filename="render.odt"'
	
    context = {'aaa': pk}

    engine = Renderer()
    template = open('doc_template/ustyazi.odt', 'rb')

    #output = open('output.odt', 'wb')
    #output.write(engine.render(template, c=context ))
    
    response.write(engine.render(template, c=context ))
    return response
    
    
