from django.shortcuts import render, redirect, get_object_or_404
from .forms import SongForm, PlaylistForm
from .models import Album, Playlist
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def signup(request):
    error_message = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("album-index")
        else:
            error_message = "Invalid sign up - try again"
    form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "signup.html", context)


class Home(LoginView):
    template_name = "home.html"


def about(request):
    return render(request, "about.html")


class PlaylistCreate(LoginRequiredMixin, CreateView):
    model = Playlist
    form_class = PlaylistForm
    template_name = "main_app/playlist_form.html"
    success_url = reverse_lazy("playlist-index")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(PlaylistCreate, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class PlaylistList(LoginRequiredMixin, ListView):
    model = Playlist
    template_name = "main_app/playlist_index.html"

    def get_queryset(self):
        return Playlist.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        playlists = self.get_queryset().prefetch_related("albums")
        context["playlists"] = playlists
        context["has_playlists"] = playlists.exists()
        return context


class PlaylistUpdate(LoginRequiredMixin, UpdateView):
    model = Playlist
    form_class = PlaylistForm
    template_name = "main_app/playlist_form.html"

    def get_queryset(self):
        return Playlist.objects.filter(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super(PlaylistUpdate, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse_lazy("playlist-index")


class PlaylistDelete(LoginRequiredMixin, DeleteView):
    model = Playlist
    success_url = reverse_lazy("playlist-index")

    def get_queryset(self):
        return Playlist.objects.filter(user=self.request.user)


class AlbumCreate(LoginRequiredMixin, CreateView):
    model = Album
    fields = ["title", "artist", "release_year", "cover_image_url"]
    success_url = "/albums/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AlbumUpdate(LoginRequiredMixin, UpdateView):
    model = Album
    fields = ["artist", "release_year", "cover_image_url"]

    def get_queryset(self):
        return Album.objects.filter(user=self.request.user)


class AlbumDelete(LoginRequiredMixin, DeleteView):
    model = Album
    success_url = reverse_lazy("album-index")

    def get_queryset(self):
        queryset = Album.objects.filter(user=self.request.user)
        return queryset
    
def home(request):
    return render(request, "home.html")


@login_required
def album_index(request):
    albums = Album.objects.filter(user=request.user)
    has_albums = albums.exists()

    return render(request, "albums/index.html", {"albums": albums, "has_albums": has_albums})

@login_required
def album_detail(request, album_id):
    album = Album.objects.get(id=album_id, user=request.user)
    songs = album.songs.all()
    playlists = album.playlists.filter(user=request.user)  
    playlists_album_doesnt_have = Playlist.objects.exclude(
        id__in=album.playlists.all().values_list("id")
    ).filter(user=request.user)
    if request.method == "POST":
        form = SongForm(request.POST)
        if form.is_valid():
            song = form.save(commit=False)
            song.album = album
            song.save()
            return redirect("album-detail", album_id=album_id)
    else:
        form = SongForm()
    return render(
        request,
        "albums/detail.html",
        {
            "album": album,
            "playlists": playlists,
            "playlists_album_doesnt_have": playlists_album_doesnt_have,
            "songs": songs,
            "form": form,
        },
    )


@login_required
def associate_playlist(request, album_id, playlist_id):
    album = get_object_or_404(Album, id=album_id, user=request.user)
    playlist = get_object_or_404(Playlist, id=playlist_id, user=request.user)
    album.playlists.add(playlist)
    return redirect("album-detail", album_id=album_id)


@login_required
def remove_playlist(request, album_id, playlist_id):
    album = get_object_or_404(Album, id=album_id, user=request.user)
    playlist = get_object_or_404(Playlist, id=playlist_id, user=request.user)
    album.playlists.remove(playlist)
    return redirect("album-detail", album_id=album.id)