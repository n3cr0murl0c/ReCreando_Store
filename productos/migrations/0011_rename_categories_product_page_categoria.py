# Generated by Django 3.2.9 on 2021-12-02 23:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0010_alter_producto_nombre_producto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_page',
            old_name='categories',
            new_name='categoria',
        ),
    ]
