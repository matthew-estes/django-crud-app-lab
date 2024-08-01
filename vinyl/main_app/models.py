from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    release_year = models.IntegerField()
    cover_image_url = models.URLField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.artist}"

    def get_absolute_url(self):
        return reverse("album-detail", kwargs={"album_id": self.id})
    
class Playlist(models.Model):
    name = models.CharField(max_length=200)
    albums = models.ManyToManyField(Album, related_name='playlists')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("playlist-detail", kwargs={"playlist_id": self.id})    
    
class Song(models.Model):
    track_number = models.CharField(max_length=2)
    title = models.CharField(max_length=200)
    album = models.ForeignKey(Album, related_name='songs', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} from {self.album.title}"

    class Meta:
        ordering = ['track_number']