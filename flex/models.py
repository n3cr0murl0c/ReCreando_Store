""" Flexible Page """
from django.db import models
from django import forms

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from modelcluster.fields import ParentalManyToManyField


from productos import my_blocks
from productos.models import producto
from wagtail_svgmap import blocks
# Create your models here.
class FlexPage(Page):
    """ Flexible page class"""
    template = "flex/flex_page.html"
    class Meta:
        verbose_name="Flex Page"
        verbose_name_plural= "Flex Pages"


    
