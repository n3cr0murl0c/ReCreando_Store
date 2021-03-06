from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.response import TemplateResponse

# Create your views here.

from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.utils import timezone
from productos.models import Order, producto
from productos.views import productos

def home(request):
    """ Funcion para obtener todos los productos y mostrarlos en paginas ordenadas en la homepage"""
    query = producto.objects.all().order_by('-pub_date')#Obtengo todos los productos
    query_featured = producto.objects.latest('pub_date')
    page = request.GET.get('page', 1)
    n_productos=producto.objects.count()
    # Search
    if query:
        #Si hay productos los divido en sets de 5
        # y los muestro en paginas distintas
        #@todo meter el submit de page
        paginator = Paginator(query, 4)
                        
        
        try:
            results = paginator.page(page)
        except PageNotAnInteger:
            results = paginator.page(1)
        except EmptyPage:
            results = paginator.page(paginator.num_pages)
        return TemplateResponse(request, 'home/home_page.html', {
            'featured':query_featured,
            'query': query,
            'results': results,
            'n_results':n_productos,
        })
      
    else:
        return TemplateResponse(request, 'home/home_page.html', {})

   