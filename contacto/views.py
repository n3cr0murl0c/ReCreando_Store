from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.response import TemplateResponse

# Create your views here.

from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.utils import timezone
from productos.models import Order, producto


# Create your views here.
def contacto(request):
    context = {
        'items': producto.objects.all()
    }
    return TemplateResponse(request, 'contacto/contacto.html', {
            'slide1': context,
        }
    )