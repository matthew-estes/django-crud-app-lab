from django import forms
from .models import Song, Playlist, Album


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ["track_number", "title"]

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ["name", "albums"]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields['albums'].queryset = Album.objects.filter(user=user)