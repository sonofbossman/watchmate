from django.urls import path
from watchlist_app.api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
  path('', views.MovieList.as_view(), name='movie-list'),
  path('<int:pk>', views.MovieDetails.as_view(), name='movie-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)