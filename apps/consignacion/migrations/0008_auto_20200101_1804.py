# Generated by Django 3.0 on 2020-01-02 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consignacion', '0007_auto_20200101_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleconsigna',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True, verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='detalleconsigna',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True, verbose_name='Total'),
        ),
    ]