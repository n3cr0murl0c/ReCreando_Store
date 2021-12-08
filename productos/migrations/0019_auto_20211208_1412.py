# Generated by Django 3.2.9 on 2021-12-08 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0018_producto_precio_descontado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='precio_descontado',
            new_name='precio_en_descuento',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='descuento_producto',
        ),
        migrations.AddField(
            model_name='producto',
            name='con_descuento',
            field=models.BooleanField(default=False),
        ),
    ]
