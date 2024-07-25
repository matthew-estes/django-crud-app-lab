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
         return reverse('album-detail', kwargs={'album_id': self.id})


