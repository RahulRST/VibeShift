from django.urls import path

from . import views

urlpatterns = [
  path('song/<int:pk>/', views.song_detail, name='song_detail'), 
  path('search/', views.home, name='search'),
]
