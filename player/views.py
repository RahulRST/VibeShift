from django.shortcuts import render, get_object_or_404

from player.models import Song

def song_list(request):
  """
  View to display a list of all songs.
  """
  songs = Song.objects.all()
  context = {'songs': songs}
  return render(request, 'music_player/song_list.html', context)

def song_detail(request, pk):
  """
  View to display details of a specific song based on its ID (pk).
  """
  song = get_object_or_404(Song, pk=pk)
  context = {'song': song}
  return render(request, 'music_player/song_detail.html', context)