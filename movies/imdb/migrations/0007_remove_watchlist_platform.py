# Generated by Django 4.2.5 on 2023-09-12 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imdb', '0006_watchlist_platform_alter_streamplatform_website_link_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='platform',
        ),
    ]