# Generated by Django 5.1.4 on 2025-01-13 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0007_alter_pago_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pago',
            name='correo',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]