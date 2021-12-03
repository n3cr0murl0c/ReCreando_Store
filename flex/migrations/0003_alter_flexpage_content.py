# Generated by Django 3.2.9 on 2021-12-02 17:02

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0002_alter_flexpage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='content',
            field=wagtail.core.fields.StreamField([('tarjeta_producto', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your Title', required=True)), ('text', wagtail.core.blocks.RichTextBlock(help_text='Add your Block Content', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('boton_ver_mas', wagtail.core.blocks.PageChooserBlock(required=False)), ('boton_comprar', wagtail.core.blocks.PageChooserBlock(required=False)), ('tag1', wagtail.core.blocks.CharBlock(help_text='Tag1', required=True)), ('tag2', wagtail.core.blocks.CharBlock(help_text='Tag2', required=True)), ('tag3', wagtail.core.blocks.CharBlock(help_text='Tag3', required=True))]))], blank=True, null=True),
        ),
    ]
