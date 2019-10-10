# Generated by Django 2.2.5 on 2019-09-29 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizador', '0007_auto_20190929_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='anual_valor_Seguro',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='deducible',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='deducible_robo',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='mensual_valor_Seguro',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='semestral_valor_Seguro',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='trimestral_valor_Seguro',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='valor',
            field=models.FloatField(default=0),
        ),
    ]
