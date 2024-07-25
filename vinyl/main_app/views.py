from django.shortcuts import render

from .models import Album
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class AlbumCreate(CreateView):
    model = Album
    fields = ["title", "artist", "release_year", "description", "cover_image_url"]
    success_url = "/albums/"


class AlbumUpdate(UpdateView):
    model = Album
    fields = ["artist", "release_year", "description", "cover_image_url"]


class AlbumDelete(DeleteView):
    model = Album
    success_url = "/albums/"


def home(request):
    return render(request, "home.html")


def album_index(request):
    albums = Album.objects.all()
    return render(request, "albums/index.html", {"albums": albums})


def album_detail(request, album_id):
    album = Album.objects.get(id=album_id)
    return render(request, "albums/detail.html", {"album": album})
