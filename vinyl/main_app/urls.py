from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("albums/", views.album_index, name="album_index"),
    path("albums/<int:album_id>/", views.album_detail, name="album_detail"),
    path("albums/create/", views.AlbumCreate.as_view(), name="album_create"),
    path(
        "albums/<int:album_id>/update/",
        views.AlbumUpdate.as_view(),
        name="album_update",
    ),
    path(
        "albums/<int:album_id>/delete/",
        views.AlbumDelete.as_view(),
        name="album_delete",
    ),
    path("albums/<int:album_id>/add_song", views.add_song, name="add_song"),
]
