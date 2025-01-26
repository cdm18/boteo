# Generated by Django 5.1.4 on 2025-01-26 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_alter_bill_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='bill',
            name='identification',
        ),
        migrations.RemoveField(
            model_name='bill',
            name='space_name',
        ),
        migrations.RemoveField(
            model_name='bill',
            name='total_amount',
        ),
        migrations.AlterField(
            model_name='bill',
            name='status',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('Pagado', 'Pagado'), ('Cancelado', 'Cancelado')], default='Pendiente', max_length=10),
        ),
    ]
