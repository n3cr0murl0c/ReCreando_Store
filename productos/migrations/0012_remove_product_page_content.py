# Generated by Django 3.2.9 on 2021-12-02 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0011_rename_categories_product_page_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_page',
            name='content',
        ),
    ]
