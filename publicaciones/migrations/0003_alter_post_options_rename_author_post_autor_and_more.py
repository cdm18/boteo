# Generated by Django 5.1.4 on 2025-01-13 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0002_alter_post_options_rename_autor_post_author_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-fecha_creacion']},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='contenido',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created_at',
            new_name='fecha_creacion',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='updated_at',
            new_name='fecha_modificacion',
        ),
    ]