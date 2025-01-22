# Generated by Django 5.1.4 on 2025-01-22 17:11

import account_settings.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(default='default_profile.png', upload_to=account_settings.models.user_profile_picture_path, verbose_name='Foto de perfil')),
                ('about_me', models.TextField(blank=True, verbose_name='Sobre mí')),
                ('stats_reservations', models.IntegerField(default=28, verbose_name='Reservas')),
                ('stats_played_hours', models.IntegerField(default=56, verbose_name='Horas jugadas')),
                ('stats_attended_events', models.IntegerField(default=12, verbose_name='Eventos asistidos')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
