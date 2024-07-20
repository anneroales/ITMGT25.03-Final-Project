from django.db import models
from django.contrib.auth.models import User

class StreamingPlatform(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Movie(models.Model):
    title = models.CharField(max_length=200, unique=True)
    year = models.IntegerField()
    platforms = models.ManyToManyField(StreamingPlatform, related_name='movies', blank=True)
    rating = models.FloatField(null=True, blank=True)
    watched = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

class Series(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    platforms = models.ManyToManyField(StreamingPlatform, related_name='series', blank=True)
    rating = models.FloatField(null=True, blank=True)
    watched = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    watched_movies = models.ManyToManyField(Movie, related_name='watched_by', blank=True)
    watched_series = models.ManyToManyField(Series, related_name='watched_by', blank=True)

    def __str__(self):
        return self.user.username
    
class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, null=True, blank=True, on_delete=models.CASCADE)
    series = models.ForeignKey(Series, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'movie', 'series')
