# Generated by Django 4.0.6 on 2022-08-05 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MoviesInventary', '0005_alter_movie_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='movie',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='usuario',
            name='edad',
            field=models.IntegerField(null=True, verbose_name='Edad'),
        ),
    ]
