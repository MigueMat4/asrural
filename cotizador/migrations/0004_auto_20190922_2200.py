# Generated by Django 2.2.5 on 2019-09-23 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizador', '0003_auto_20190922_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotizacion',
            name='accidentes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='lesiones',
            field=models.IntegerField(default=0),
        ),
    ]
