from datetime import date
from django.shortcuts import render, get_object_or_404

from player.models import Song

def home(request):
  songs = Song.objects.all()
  search_query = request.GET.get('query', '')
  if search_query:
    songs = songs.filter(title__icontains=search_query)
  context = {'songs': songs, 'search_query': search_query, 'current_year': date.today().year}
  return render(request, 'music_player/home.html', context)

def song_detail(request, pk):
  song = get_object_or_404(Song, pk=pk)
  context = {'song': song}
  return render(request, 'music_player/song_detail.html', context)