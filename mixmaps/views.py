from django.shortcuts import render
from django.conf import settings
import googlemaps
from datetime import datetime


gmaps = googlemaps.Client(key=settings.GOOGLE_API_KEY)
# Create your views here.
