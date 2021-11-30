# Generated by Django 3.2.9 on 2021-11-29 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailsvg', '0005_alter_svg_file'),
        ('home', '0011_alter_homepage_logo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='logo_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailsvg.svg'),
        ),
    ]