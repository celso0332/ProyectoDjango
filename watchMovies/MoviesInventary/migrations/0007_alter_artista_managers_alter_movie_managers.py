# Generated by Django 4.0.6 on 2022-08-06 19:29

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('MoviesInventary', '0006_alter_movie_managers_usuario_edad'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='artista',
            managers=[
                ('OperacionesManager3', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='movie',
            managers=[
                ('OperacionesManager', django.db.models.manager.Manager()),
            ],
        ),
    ]
