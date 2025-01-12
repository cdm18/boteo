# Generated by Django 5.1.4 on 2025-01-12 04:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('areas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SportsSpace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sport_type', models.CharField(choices=[('Fútbol', 'Fútbol'), ('Basketball', 'Basketball'), ('Piscina', 'Piscina'), ('Gym', 'Gym'), ('Ecuavoley', 'Ecuavoley')], default=('Fútbol', 'Fútbol'), max_length=100, verbose_name='Tipo de Deporte')),
                ('length', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('width', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('surface', models.CharField(choices=[('Sintética', 'Sintética'), ('Pasto Natural', 'Pasto Natural')], default='Sintética', max_length=16, verbose_name='Tipo de Superficie')),
                ('recommended_capacity', models.IntegerField(blank=True, null=True, verbose_name='Capacidad')),
                ('cost_per_hour', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='css', to='areas.area')),
            ],
        ),
    ]