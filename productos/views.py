from django.shortcuts import render

# Create your views here.

from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.utils import timezone
from .models import producto

def item_list(request):
    context = {
        'items': producto.objects.all()
    }
    return render(request,
        'productos/item_list.html',
        context)

def productos(request):
    
    

    return TemplateResponse(request, 'productos/productos.html', {
        #Variables a hacer parsing en el template
    })
