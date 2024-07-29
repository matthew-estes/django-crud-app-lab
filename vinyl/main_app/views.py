from django.shortcuts import render, redirect, get_object_or_404
from .forms import SongForm
from .models import Album, Song
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
    album = get_object_or_404(Album, pk=album_id)
    songs = album.songs.all()  # Retrieve all songs related to this album
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            new_song = form.save(commit=False)
            new_song.album = album
            new_song.save()
            return redirect('album_detail', album_id=album.id)
    else:
        form = SongForm()
    return render(request, 'albums/detail.html', {'album': album, 'songs': songs, 'form': form})