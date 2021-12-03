from django.shortcuts import render

# Create your views here.
import calendar

from django.http import HttpResponse
from django.utils import timezone


def productos(request):
    current_year = timezone.now().year
    calendar_html = calendar.HTMLCalendar().formatyear(current_year)

    return render(request, 'productos/productos.html', {
        'current_year': current_year,
        'calendar_html': calendar_html,
    })
