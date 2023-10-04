from django.urls import path, include
# from imdb.api.views import movie_list, each_movie_list
# from imdb.api.views import MovieListAv, MovieDetailsAv
from imdb.api import views
from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     path('list/', movie_list, name = 'movie_list'),
#     path('<int:pk>', each_movie_list, name = 'each_movie_list'),
# ]

# above one we used for function based view.. !!!

# urlpatterns = [
#     path('list/', MovieListAv.as_view(), name = 'movie_list'),
#     path('<int:pk>', Movie unique=True, blank=False,null=FalseDetailsAv.as_view(), name = 'each_movie_list'),
# ]

# for the Class based view w unique=True, blank=False,null=False are using ""as.view()"" function to call the class..[which is converting into a view]

# urlpatterns =[
#     path('list/', views.WatchListListView, name = 'Movie_list'),
#     path('<int:pk>',views.WatchListDetailsView, name = 'Movie_Details'),
#     path('ott/', views.StreamPlatformListView, name = 'Platform_Stream'),
#     path('ott/<int:pk>',views.StreamPlatformDetailsView, name='Platform_List'),
# ]
router = DefaultRouter()
router.register('stream', views.StreamPlatformViewVS, basename='stream')


urlpatterns = [
    path('movies/', views.WatchListViewAv.as_view(), name = 'movie-list'),
    path('movie-create/', views.WatchlistCreateViewAv.as_view(), name = 'movie-create'),
    path('<int:pk>', views.WatchListDetailsViewAv.as_view(), name = 'movie-detail'), # 'streamplatform-detail' when we use hyperlinkmodelserializer

    # path('streams/', views.StreamPlatformListViewAv.as_view(), name = 'stream-list'),
    # path('stream/<int:pk>/', views.StreamPlatformDetailsViewAv.as_view(), name = 'stream-detail'),
    
    # path('reviews/', views.ReviewListViewAv.as_view(), name = 'review-list'),
    # path('review/<int:pk>/', views.ReviewDetailViewAv.as_view(), name='review-detail'),
    path('', include(router.urls)),

    path('<int:pk>/review-create', views.ReviewsCreateViewAv.as_view(),name = 'review-create'),
    path('<int:pk>/reviews', views.ReviewListViewAv.as_view(), name='review-list'),
    path('review/<int:pk>', views.ReviewDetailViewAv.as_view(), name = 'review-detail'),
    
]
