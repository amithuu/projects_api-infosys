from django.urls import path
# from imdb.api.views import movie_list, each_movie_list
from imdb.api.views import MovieListAv, MovieDetailsAv

# urlpatterns = [
#     path('list/', movie_list, name = 'movie_list'),
#     path('<int:pk>', each_movie_list, name = 'each_movie_list'),
# ]

# above one we used for function based view.. !!!

urlpatterns = [
    path('list/', MovieListAv.as_view(), name = 'movie_list'),
    path('<int:pk>', MovieDetailsAv.as_view(), name = 'each_movie_list'),
]

# for the Class based view we are using ""as.view()"" function to call the class..[which is converting into a view]



