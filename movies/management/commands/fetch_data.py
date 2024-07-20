#This is a semi-failed code, it kinda works, but not the way I want it to.

from django.core.management.base import BaseCommand
from imdb import Cinemagoer
from movies.models import Movie, StreamingPlatform
import requests

TMDB_API_KEY = '884949b9fcb23c7c45e11eb5f6089652' 

class Command(BaseCommand):
    help = 'Fetch movies data from IMDb using Cinemagoer'

    def handle(self, *args, **kwargs):
        ia = Cinemagoer()
        top_movies = ia.get_top250_movies()  

        for movie in top_movies:
            print(f"Processing movie: {movie['title']}")  

            
            assigned_platform = None

            
            try:
                tmdb_response = requests.get(
                f'https://api.themoviedb.org/3/movie/{movie.movieID}/watch/providers?api_key={TMDB_API_KEY}'
            )
                streaming_info = tmdb_response.json()
                print(f"Streaming info for {movie['title']}: {streaming_info}")

               
                if 'results' in streaming_info and 'US' in streaming_info['results']:
                    for provider in streaming_info['results']['US'].get('flatrate', []):
                        assigned_platform, _ = StreamingPlatform.objects.get_or_create(name=provider['provider_name'])
                        break  
                else:
                        print(f"No streaming platforms found for {movie['title']}.")
            except requests.exceptions.RequestException as e:
                print(f"Error fetching streaming info for {movie['title']}: {e}")          
            
           
            movie_obj, created = Movie.objects.update_or_create(
                title=movie['title'],
                defaults={
                    'year': movie['year'],
                    'rating': movie.get('rating', None),
                    'platform': assigned_platform, 
                    'watched': False 
                }
            )
            if created:
                print(f"Added movie: {movie['title']}")
            else:
                print(f"Updated movie: {movie['title']}")

        self.stdout.write(self.style.SUCCESS("Successfully fetched data for top movies."))