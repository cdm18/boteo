# Generated by Django 5.1.4 on 2025-01-13 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0003_alter_post_options_rename_author_post_autor_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at']},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='autor',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='contenido',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='fecha_creacion',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='fecha_modificacion',
            new_name='updated_at',
        ),
    ]
