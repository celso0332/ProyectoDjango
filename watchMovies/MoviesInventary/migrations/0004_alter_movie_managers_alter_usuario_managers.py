# Generated by Django 4.0.6 on 2022-08-05 03:43

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('MoviesInventary', '0003_alter_movie_portada'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='movie',
            managers=[
                ('OperacionesManager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='usuario',
            managers=[
                ('OperacionesManager2', django.db.models.manager.Manager()),
            ],
        ),
    ]