from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from secretary import Renderer

from .models import Ustyazi


def index(request):
    context = {'aaa': 'bbb'}
    return render(request, 'ustyazi/index.html', context)


class Ustyazi_List(ListView):
    model = Ustyazi
    

class Ustyazi_Create(SuccessMessageMixin, CreateView):
    model = Ustyazi
    fields = ['dosya_no', 'sayi_no', 'tarih', 'konu', 'nereye', 'ilgi', 'yazi', 'ek']
    success_url = reverse_lazy('ustyazi-liste')
    success_message = 'Başarıyla kaydedildi...'
    
    
class Ustyazi_Update(SuccessMessageMixin, UpdateView):
    model = Ustyazi
    fields = ['dosya_no', 'sayi_no', 'tarih', 'konu', 'nereye', 'ilgi', 'yazi', 'ek']
    success_url = reverse_lazy('ustyazi-liste')
    success_message = 'Başarıyla kaydedildi...'


class Ustyazi_Delete(DeleteView):
    model = Ustyazi
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
    
    
