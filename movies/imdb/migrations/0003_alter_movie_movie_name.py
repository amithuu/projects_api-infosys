# Generated by Django 4.2.5 on 2023-09-11 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imdb', '0002_alter_movie_movie_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_name',
            field=models.CharField(max_length=20),
        ),
    ]
