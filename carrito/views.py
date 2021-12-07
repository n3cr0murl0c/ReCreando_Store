from django.shortcuts import render
from productos.models import producto
# Create your views here.
def carrito(request):
    context = {
        'items': producto.objects.all()
    }
    return render(request,
        'cart/cart.html',
        context)