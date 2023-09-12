# Generated by Django 4.2.5 on 2023-09-12 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imdb', '0005_streamplatform_watchlist_delete_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='platform',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='watchlist', to='imdb.streamplatform'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='streamplatform',
            name='website_link',
            field=models.URLField(max_length=100),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='movie_desc',
            field=models.CharField(max_length=150),
        ),
    ]