from django.db import models

# Create your models here.
class tipos_docs(models.Model):
    tipo=models.CharField(max_length=50,blank=False, null=False)
    # tipo2=models.CharField(max_length=50,blank=False, null=False, default="PASAPORTE")
    # tipo3=models.CharField(max_length=50,blank=False, null=False, default="OTRO")
    def __str__(self):
        return "%s" % (self.tipo)

class Cliente(models.Model):
    """docstring for Clientes."""
    email = models.EmailField(max_length=250,blank=False, null=False)
    nombre = models.CharField(max_length=50,blank=False, null=False)
    apellido = models.CharField(max_length=50,blank=False, null=False)
    telefono = models.CharField(max_length=20,blank=False, null=False)
    tipo_documento = models.ForeignKey(tipos_docs,on_delete=models.CASCADE)
    documento = models.CharField(max_length=20,blank=False, null=False)
    direccion1 = models.CharField(max_length=150,blank=False, null=False)
    direccion2 = models.CharField(max_length=150,blank=True, null=False)
    activo = models.BooleanField(null=True, blank=False)


    def __str__(self):
        """representacion en string del objeto"""
        return "%s %s" % (self.nombre,self.apellido)
