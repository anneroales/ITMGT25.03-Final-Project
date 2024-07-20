from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Series, UserProfile, StreamingPlatform, Watchlist
from .forms import MovieForm, SeriesForm

def home_view(request):
    if request.user.is_authenticated:
        return redirect('profile')
    return render(request, 'movies/home.html')

def profile_view(request):
    profile = UserProfile.objects.get(user=request.user)
    watched_movies = Movie.objects.filter(watched=True)
    watched_series = Series.objects.filter(watched=True)
    watchlist_items = Watchlist.objects.filter(user=request.user)
    unwatched_movies = Movie.objects.filter(watched=False, user=request.user).exclude(id__in=watchlist_items.values_list('movie', flat=True))
    unwatched_series = Series.objects.filter(watched=False, user=request.user).exclude(id__in=watchlist_items.values_list('series', flat=True))
    streaming_services = StreamingPlatform.objects.all()
    context = {
        'user': request.user,
        'watched_movies': watched_movies,
        'unwatched_movies': unwatched_movies,
        'watched_series': watched_series,
        'unwatched_series': unwatched_series,
        'streaming_services': streaming_services,
        'watchlist_items': watchlist_items,
    }
    return render(request, 'movies/profile.html', context)

def movie_list_view(request):
    movies = Movie.objects.filter(user=request.user)
    return render(request, 'movies/movie_list.html', {'movies':movies})

def series_list_view(request):
    series = Series.objects.filter(user=request.user)
    return render(request, 'movies/series_list.html', {'series': series})

def mark_movies_watched(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    movie.watched = not movie.watched  
    movie.save()
    return redirect('movies')

def mark_movies_unwatched(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    movie.watched = False  
    movie.save()
    return redirect('movies')

def unwatched_movies(request):
    movies = Movie.objects.filter(watched=False, user=request.user)
    return render(request, 'movies/unwatched_movies.html', {'movies': movies})

def watched_movies(request):
    movies = Movie.objects.filter(watched=True, user=request.user)
    return render(request, 'movies/watched_movies.html', {'movies': movies})

def unwatched_series(request):
    series = Series.objects.filter(watched=False, user=request.user)
    return render(request, 'movies/unwatched_series.html', {'series': series})

def watched_series(request):
    series = Series.objects.filter(watched=True, user=request.user)
    return render(request, 'movies/watch_series.html', {'series': series})

def mark_series_watched(request, series_id):
    series = Series.objects.get(id=series_id)
    series.watched = not series.watched
    series.save()
    return redirect('series_list')

def mark_series_unwatched(request, series_id):
    series = Series.objects.get(id=series_id)
    series.watched = False  
    series.save()
    return redirect('series_list')

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user  
            movie.save()
            return redirect('profile')  
    else:
        form = MovieForm()
    return render(request, 'movies/add_movie.html', {'form': form})

def add_series(request):
    if request.method == 'POST':
        form = SeriesForm(request.POST)
        if form.is_valid():
            series = form.save(commit=False)
            series.user = request.user  
            series.save()
            return redirect('profile') 
    else:
        form = SeriesForm()
    return render(request, 'movies/add_series.html', {'form': form})

def edit_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    form = MovieForm(instance=movie)  
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            if 'add_to_watchlist' in request.POST:
                Watchlist.objects.get_or_create(user=request.user, movie=movie)
            return redirect('profile') 
    return render(request, 'movies/edit_movie.html', {'form': form, 'movie': movie})

def edit_series(request, series_id):
    series = get_object_or_404(Series, id=series_id)
    form = SeriesForm(instance=series)  
    if request.method == 'POST':
        form = SeriesForm(request.POST, instance=series)  
        if form.is_valid():
            form.save()  
            if 'add_to_watchlist' in request.POST:
                Watchlist.objects.get_or_create(user=request.user, series=series)
            return redirect('profile')  
    return render(request, 'movies/edit_series.html', {'form': form, 'series': series})

def add_to_watchlist(request, item_id, item_type):
    if request.method == 'POST':
        if item_type == 'movie':
            movie = get_object_or_404(Movie, id=item_id)
            Watchlist.objects.get_or_create(user=request.user, movie=movie)
        elif item_type == 'series':
            series = get_object_or_404(Series, id=item_id)
            Watchlist.objects.get_or_create(user=request.user, series=series)
    return redirect('profile')