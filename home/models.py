from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
#para bold or italic
from wagtail.core.fields import RichTextField

from wagtailsvg.models import Svg
from wagtailsvg.blocks import SvgChooserBlock
from wagtailsvg.edit_handlers import SvgChooserPanel

class HomePage(Page):
    """Home Page Model"""
    template = "home/home_page.html"
    max_count = 1 #Solo se puede tener una sola pagina home
    page_title = models.CharField(max_length=50, blank=False, null=True)
    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_subtitle = RichTextField(
        features=["bold", "italic"],
        null=True,
        blank=True,
    )
    
    banner_description=models.CharField(max_length=250, blank=False, null=True)
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,#no se quiere que nada mas se borre
        related_name="+"
    )
    search_image = models.ForeignKey(
        Svg,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,#no se quiere que nada mas se borre
        related_name="+"
    )
    banner_cta=models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,#no se quiere que nada mas se borre
        related_name="+"
    )
    logo_image = models.ForeignKey(
        Svg,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    # logo_image = models.ForeignKey(
    #     "wagtailimages.Image",
    #     null=True,
    #     blank=False,
    #     on_delete=models.SET_NULL,#no se quiere que nada mas se borre
    #     related_name="+"
    # )
    # Si se tiene un char field, se debe agregar eso en wagtail tambien


    #Esto es wagtail, para agergar conteneido en la parte de admin
    content_panels = Page.content_panels + [
        FieldPanel("page_title"),
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        FieldPanel("banner_description"),
        ImageChooserPanel("banner_image"),
        SvgChooserPanel("search_image"),
        SvgChooserPanel("logo_image"),
        PageChooserPanel("banner_cta")
    ]
    #Metadata
    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
