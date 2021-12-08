from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register,
)
from .models import producto

class productoAdmin(ModelAdmin):
    """docstring for producto_admin."""
    model = producto
    menu_label = "Productos"
    menu_icon = "folder"
    menu_order = 6
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display =("ID","stock", "nombre_producto","descripcion_producto","precio_producto","precio_en_descuento","con_descuento")
    search_fields = ("ID","stock", "nombre_producto","descripcion_producto","precio_producto","precio_en_descuento","con_descuento")

modeladmin_register(productoAdmin)
