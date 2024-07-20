from django.urls import path
from .views import profile_view, mark_movies_watched, mark_series_watched, home_view, movie_list_view, series_list_view, unwatched_movies, watched_movies, add_movie, add_series, unwatched_series, watched_series, edit_movie, edit_series,  mark_movies_unwatched,  mark_series_unwatched, add_to_watchlist


urlpatterns = [
    path('', home_view, name='home'),
    path('accounts/profile/', profile_view, name='profile'),
    path('movies/unwatched/', unwatched_movies, name='unwatched_movies'),
    path('movies/watched/', watched_movies, name='watched_movies'),
    path('movies/', movie_list_view, name='movies'),
    path('movies/<int:movie_id>/mark-watched/', mark_movies_watched, name='mark_movies_watched'),
    path('movies/mark-unwatched/<int:movie_id>/', mark_movies_unwatched, name='mark_movies_unwatched'),
    path('series/', series_list_view, name='series'),
    path('series/<int:series_id>/mark-watched/', mark_series_watched, name='mark_series_watched'),
    path('series/mark-unwatched/<int:series_id>/', mark_series_unwatched, name='mark_series_unwatched'),
    path('add-movie/', add_movie, name='add_movie'),
    path('add-series/', add_series, name='add_series'),
    path('series/unwatched/', unwatched_series, name='unwatched_series'),
    path('series/watched/', watched_series, name='watched_series'),
    path('edit-movie/<int:movie_id>/', edit_movie, name='edit_movie'),
    path('edit-series/<int:series_id>/', edit_series, name='edit_series'),
    path('watchlist/add/<int:item_id>/<str:item_type>/', add_to_watchlist, name='add_to_watchlist'),
]