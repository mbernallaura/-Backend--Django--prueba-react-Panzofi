# Generated by Django 4.2 on 2023-04-19 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appiPanzofi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='cod_rol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appiPanzofi.rol'),
        ),
    ]
