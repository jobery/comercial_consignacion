# Generated by Django 3.0 on 2019-12-31 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consignacion', '0004_remove_vendedor_credito'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='TipoArticulo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='consignacion.TipoArticulo'),
        ),
    ]