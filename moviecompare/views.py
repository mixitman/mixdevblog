from django.shortcuts import render
from django.conf import settings

from .forms import MovieSearch
import tmdbsimple as tmdb

tmdb.API_KEY = settings.TMDB_API_KEY


def search_movie(request):
    """
    Search movie title and return 5 pages of results
    """
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
            for i in range(2, 5 + 1):
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
    else:
        form = MovieSearch()

    return render(request, './moviecompare/compare.html', {"form": form})


def get_movie(request, movid):
    """
    from search/movie results, get details by movie id (movid)
    """
    movie = tmdb.Movies(movid)
    response = movie.info()
    context = {
        'response': response
    }
    return render(request, './moviecompare/detail.html', context)


# def post_detail(request, slug=None):
#     instance = get_object_or_404(Post, slug=slug)
#     if instance.published_date > timezone.now() or instance.draft:
#         if not request.user.is_staff or not request.user.is_superuser:
#             raise Http404
#     context = {
#         'title': instance.title,
#         'instance': instance,
#     }
#     return render(request, './blog/detail.html', context)
