# Generated by Django 4.2.5 on 2023-09-20 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imdb', '0010_review_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='avr_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='total_ratings',
            field=models.IntegerField(default=0),
        ),
    ]
