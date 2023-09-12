from django.urls import path
# from imdb.api.views import movie_list, each_movie_list
# from imdb.api.views import MovieListAv, MovieDetailsAv
from imdb.api import views

# urlpatterns = [
#     path('list/', movie_list, name = 'movie_list'),
#     path('<int:pk>', each_movie_list, name = 'each_movie_list'),
# ]

# above one we used for function based view.. !!!

# urlpatterns = [
#     path('list/', MovieListAv.as_view(), name = 'movie_list'),
#     path('<int:pk>', MovieDetailsAv.as_view(), name = 'each_movie_list'),
# ]

# for the Class based view we are using ""as.view()"" function to call the class..[which is converting into a view]

# urlpatterns =[
#     path('list/', views.WatchListListView, name = 'Movie_list'),
#     path('<int:pk>',views.WatchListDetailsView, name = 'Movie_Details'),
#     path('ott/', views.StreamPlatformListView, name = 'Platform_Stream'),
#     path('ott/<int:pk>',views.StreamPlatformDetailsView, name='Platform_List'),
# ]

urlpatterns = [
    path('movielist/', views.WatchListViewAv.as_view(), name = 'Movie_list'),
    path('movie<int:pk>/', views.WatchListDetailsViewAv.as_view(), name = 'Movie_Details'),
    path('streamlist/', views.StreamPlatformListViewAv.as_view(), name = 'Platform_Stream'),
    path('stream<int:pk>/', views.StreamPlatformDetailsViewAv.as_view(), name = 'Platform_Details'),
]

