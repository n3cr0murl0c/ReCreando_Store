# Generated by Django 3.2.9 on 2021-12-02 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0007_auto_20211202_1828'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='SKU',
            new_name='ID',
        ),
        migrations.AddField(
            model_name='producto',
            name='categoria_producto',
            field=models.ManyToManyField(to='productos.categoria'),
        ),
    ]
