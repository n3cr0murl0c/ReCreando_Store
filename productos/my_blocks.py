"""streamfields live in here"""

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class tarjeta_producto(blocks.StructBlock):
    """docstring for Title_and_Text_block."""
    class Meta:
        template =  "productos/tarjeta_producto.html"
        icon = "edit"
        label = "Tarjeta de Producto"

    # title = models.CharField
    title=blocks.CharBlock(
        required=True,
        help_text= 'Add your Title'
    )
    text=blocks.RichTextBlock(
        required=True,
        help_text= 'Add your Block Content'
    )
    image=ImageChooserBlock(required=True)
    boton_ver_mas = blocks.PageChooserBlock(required=False)
    boton_comprar = blocks.PageChooserBlock(required=False)
    
