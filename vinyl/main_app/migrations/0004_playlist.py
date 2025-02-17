# Generated by Django 5.0.7 on 2024-07-29 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_song_options_remove_song_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('albums', models.ManyToManyField(related_name='playlists', to='main_app.album')),
            ],
        ),
    ]
