# Generated by Django 3.2.9 on 2021-12-03 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0012_remove_product_page_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='distribuidor',
        ),
    ]
