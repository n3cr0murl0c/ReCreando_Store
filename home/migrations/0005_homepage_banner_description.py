# Generated by Django 3.2.9 on 2021-11-29 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20211129_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='banner_description',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
