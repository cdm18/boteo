# Generated by Django 5.1.4 on 2025-01-21 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('areas', '0003_alter_area_images'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='area',
            options={'permissions': [('view_all_areas', 'Can view all areas')]},
        ),
    ]
