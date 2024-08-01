from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path("albums/", views.album_index, name="album-index"),
    path("albums/<int:album_id>/", views.album_detail, name="album-detail"),
    path("albums/create/", views.AlbumCreate.as_view(), name="album-create"),
    path("albums/<int:pk>/update/", views.AlbumUpdate.as_view(), name="album-update"),
    path("albums/<int:pk>/delete/", views.AlbumDelete.as_view(), name="album-delete"), 
    path("playlists/create/", views.PlaylistCreate.as_view(), name="playlist-create"),
    path("playlists/", views.PlaylistList.as_view(), name="playlist-index"),
    path("playlists/<int:pk>/update/", views.PlaylistUpdate.as_view(), name="playlist-update"),
    path("playlists/<int:pk>/delete/", views.PlaylistDelete.as_view(), name="playlist-delete"),
    path("albums/<int:album_id>/associate-playlist/<int:playlist_id>/", views.associate_playlist, name="associate-playlist"),
    path("albums/<int:album_id>/remove-playlist/<int:playlist_id>/", views.remove_playlist, name="remove-playlist"),
    path('accounts/signup/', views.signup, name='signup'),
]