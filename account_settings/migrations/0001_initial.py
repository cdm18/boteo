# Generated by Django 5.1.4 on 2025-01-29 15:26

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
                ('profile_picture', models.ImageField(upload_to=account_settings.models.user_profile_picture_path, verbose_name='Foto de perfil')),
                ('about_me', models.TextField(blank=True, verbose_name='Sobre mí')),
                ('favorite_sports', models.CharField(blank=True, max_length=255, verbose_name='Deportes favoritos')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
