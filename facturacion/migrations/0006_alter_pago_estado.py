# Generated by Django 5.1.4 on 2025-01-12 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0005_alter_pago_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pago',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('pagado', 'Pagado')], default='pendiente', max_length=10),
        ),
    ]