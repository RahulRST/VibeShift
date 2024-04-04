from django.urls import path

from VibeShift import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
  path('', views.song_list, name='song_list'),  # List all songs
  path('song/<int:pk>/', views.song_detail, name='song_detail'), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
