# Generated by Django 3.2.9 on 2021-12-02 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tipos_docs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo1', models.CharField(max_length=50)),
                ('tipo2', models.CharField(max_length=50)),
                ('tipo3', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=250)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20)),
                ('documento', models.CharField(max_length=20)),
                ('direccion1', models.CharField(max_length=150)),
                ('direccion2', models.CharField(blank=True, max_length=150)),
                ('activo', models.BooleanField(null=True)),
                ('tipo_documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.tipos_docs')),
            ],
        ),
    ]
