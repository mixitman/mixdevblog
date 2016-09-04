from django.shortcuts import render
from django.conf import settings
from .forms import MovieSearch
import tmdbsimple as tmdb

tmdb.API_KEY = settings.TMDB_API_KEY


def search_movie(request):
    parsed_data = {'results': []}
    if request.method == 'POST':
        form = MovieSearch(request.POST)
        if form.is_valid():
            search = tmdb.Search()
            query = form.cleaned_data['moviename']
            response = search.movie(query=query)
            for movie in response['results']:
                parsed_data['results'].append(
                    {
                        'title': movie['title'],
                        'id': movie['id'],
                        'poster_path': movie['poster_path'],
                        'release_date': movie['release_date'][:-6],
                        'popularity': movie['popularity'],
                        'overview': movie['overview']
                    }
                )
            total_pages = response['total_pages']
            for i in range(2, total_pages + 1):
                response = search.movie(query=query, page=i)
                for movie in response['results']:
                    parsed_data['results'].append(
                        {
                            'title': movie['title'],
                            'id': movie['id'],
                            'poster_path': movie['poster_path'],
                            'release_date': movie['release_date'][:-6],
                            'popularity': movie['popularity'],
                            'overview': movie['overview']
                        }
                    )
            context = {
                "form": form,
                "parsed_data": parsed_data
            }
            return render(request, './moviecompare/movies.html', context)
    else:
        form = MovieSearch()

    return render(request, './moviecompare/compare.html', {"form": form})
