from datetime import date
from django.shortcuts import render, get_object_or_404

from player.models import Song, User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegistrationForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            print("Done")
            if user:
                login(request, user)
                return redirect('home')  # Redirect to your home page after login
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'music_player/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after registration
    else:
        form = RegistrationForm()
    return render(request, 'music_player/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def home(request):
  songs = Song.objects.all()
  search_query = request.GET.get('query', '')
  if search_query:
    songs = songs.filter(title__icontains=search_query)
  context = {'songs': songs, 'search_query': search_query, 'current_year': date.today().year}
  return render(request, 'music_player/home.html', context)