# Generated by Django 3.2.9 on 2021-12-02 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0005_auto_20211202_1730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flexpage',
            name='productoss',
        ),
    ]