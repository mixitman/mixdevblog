from django import forms


class MovieSearch(forms.Form):
    moviename = forms.CharField(label="Search", max_length=250)
