# Generated by Django 2.2.5 on 2019-09-29 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizador', '0005_cotizacion_deducible_robo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='deducible',
            field=models.DecimalField(decimal_places=2, default=2000.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='deducible_robo',
            field=models.DecimalField(decimal_places=2, default=2000.0, max_digits=9),
        ),
    ]
