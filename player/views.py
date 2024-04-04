from django.shortcuts import render, get_object_or_404
from .models import Song  # Assuming you have a Song model

def song_list(request):
  """
  View to display a list of all songs.
  """
  songs = Song.objects.all()  # Fetch all songs from the database
  context = {'songs': songs}
  return render(request, 'music_player/song_list.html', context)

def song_detail(request, pk):
  """
  View to display details of a specific song based on its ID (pk).
  """
  song = get_object_or_404(Song, pk=pk)  # Get the song object or raise a 404 error if not found
  context = {'song': song}
  return render(request, 'music_player/song_detail.html', context)
