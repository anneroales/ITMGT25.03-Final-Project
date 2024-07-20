from django import forms
from .models import Movie, Series, StreamingPlatform

class MovieForm(forms.ModelForm):
    platforms = forms.ModelMultipleChoiceField(
        queryset=StreamingPlatform.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False 
    )

    class Meta:
        model = Movie
        fields = ['title', 'year', 'platforms', 'watched']

class SeriesForm(forms.ModelForm):
    platforms = forms.ModelMultipleChoiceField(
        queryset=StreamingPlatform.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False  
    )

    class Meta:
        model = Series
        fields = ['title', 'year', 'platforms', 'watched']