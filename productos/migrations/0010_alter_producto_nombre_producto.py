# Generated by Django 3.2.9 on 2021-12-02 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0009_rename_categoria_producto_producto_categorias_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='nombre_producto',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
