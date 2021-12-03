from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register,
)
from .models import Cliente

class clienteAdmin(ModelAdmin):
    """docstring for cliente_admin."""
    model = Cliente
    menu_label = "Clientes"
    menu_icon = "folder"
    menu_order = 5
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display =("email", "nombre","apellido","telefono","tipo_documento","documento","direccion1","direccion2","activo",)
    search_fields = ("email", "nombre","apellido","telefono","tipo_documento","documento","direccion1","direccion2","activo",)

modeladmin_register(clienteAdmin)
