from django.db import models
from django import forms

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey, ParentalManyToManyField

from .my_blocks import tarjeta_producto

##################################
#Modelo de la PAgina web
class product_page(Page):
    """ Flexible page class"""
    template = "productos/productos.html"

    categoria = ParentalManyToManyField("categoria", blank=True)
    # content = StreamField(
    #     [
    #         ("tarjeta_producto", tarjeta_producto()),
    #     ],
    #     null = True,
    #     blank = True
    # )

    subtitle = models.CharField(max_length=100, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        MultiFieldPanel(
            [
                FieldPanel("categoria",widget=forms.CheckboxSelectMultiple)
            ],
            heading="Categoría"
        )
    ]

    class Meta:
        verbose_name="Producto"
        verbose_name_plural= "Productos"
#####################################
#Modelos de Base de Datos django
class distribuidor(models.Model):
    nombre_compania = models.CharField(max_length=50,blank=False, null=False)
    nombre_contacto = models.CharField(max_length=50,blank=False, null=False)
    apellido_contacto = models.CharField(max_length=50,blank=False, null=False)
    email_contacto = models.EmailField(max_length=250,blank=False, null=False)
    direccion_compania = models.CharField(max_length=50,blank=False, null=False)
    ciudad_compania = models.CharField(max_length=50,blank=False, null=False)
    provincia_compania = models.CharField(max_length=50,blank=False, null=False)
    pais_compania = models.CharField(max_length=50,blank=False, null=False)
    telefono_compania = models.CharField(max_length=50,blank=False, null=False)


class categoria(models.Model):
    """"Categorias para los distintos Productos"""

    name = models.CharField(max_length=50,blank=False, null=False)
    slug = models.SlugField(
        verbose_name ="slug",
        allow_unicode = True,
        max_length = 255,
        help_text = 'Slug para identificar productos por esta categoría',

    )
    panels = [
        FieldPanel("name"),
        FieldPanel("slug"),
    ]
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["name"]
    def __str__ (self):
        return self.name

class producto(models.Model):
    """Def de Producto"""
    ID = models.AutoField(primary_key=True, unique=True, null=False, blank=False)
    stock = models.IntegerField(null=True,blank=True,help_text="cantidad de unidades disponibles")
    nombre_producto = models.CharField(max_length=50,blank=False, null=False, unique=True)
    descripcion_producto = models.TextField(blank=False, null=False)
    precio_producto = models.DecimalField(max_digits=19, decimal_places=3)
    imagen_producto = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,#no se quiere que nada mas se borre
        related_name="+"
    )
    categorias_producto = models.ManyToManyField(categoria)
    distribuidor= models.ForeignKey(distribuidor,on_delete=models.CASCADE, blank=True, null=True)
register_snippet(categoria)
