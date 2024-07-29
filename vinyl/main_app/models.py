from django.db import models
from django.urls import reverse


class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    release_year = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    cover_image_url = models.URLField(max_length=255)

    def __str__(self):
        return f"{self.title} by {self.artist}"

    def get_absolute_url(self):
        return reverse("album-detail", kwargs={"album_id": self.id})
    
class Song(models.Model):
    title = models.CharField(max_length=200)
    album = models.ForeignKey(Album, related_name='songs', on_delete=models.CASCADE)
    track_number = models.IntegerField()

    def __str__(self):
        return f"{self.title} from {self.album.title}"

    class Meta:
        ordering = ['track_number']


class Playlist(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    albums = models.ManyToManyField(Album, related_name='playlists')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("playlist-detail", kwargs={"playlist_id": self.id})