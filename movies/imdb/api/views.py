from django.shortcuts import get_object_or_404
from imdb.models import WatchList, StreamPlatform, Review
from rest_framework.exceptions import ValidationError
from imdb.api.serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from imdb.api.permissions import AdminOrReadonly, ReviewUserOrReadonly
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle


# @api_view()
# @permission_classes([IsAuthenticated])
# def movie_list(request):
#     movies = Movie.objects.all()  
#             #  -> getting the data
#     serializer = MovieSerializer(movies, many=True)   
#                 # -> converting complex data into python dictionary [that is done by serializers]
#                 # i got an error attribute not found like that, so as serializer is not able to fetch all data, we need to ADD [many=True]!!!!
#     return Response(serializer.data)     
#                 # -> returning the json response

# @api_view()
# def each_movie_list(request, pk):
#     movie = Movie.objects.get(pk=pk)
#     serializer = MovieSerializer(movie)
#     return Response(serializer.data)

# #[@API_VIEW()THIS IS AN DECORATOR WHERE IF WE NEED TO GET THE DATA IN REST_FRAMEWORK VIEW WE NEED TO ADD THIS DECORATOR, 
# # WHICH TELLS WE ARE DOING [GET/POST/DELETE/PUT] FUNCTION ]


# [above is basic one]

# @api_view(['GET', 'POST'])
# def movie_list(request):

#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# @api_view(['GET', 'PUT', 'DELETE'])
# def each_movie_list(request, pk):

#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response('Error', status=status.HTTP_404_NOT_FOUND)
        
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
    
    
#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     if request.method == 'DELETE':
#         movie= Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# [Above was the Function based serializer]


# class MovieListAv(APIView):

#     def get(self, request):
        #   permission_classes = [IsAuthenticated]
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many = True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = MovieSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
# class MovieDetailsAv(APIView):

#     def get(self, request, pk ):
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         try:
#             movie = Movie.objects.get(pk=pk)
#             serializer = MovieSerializer(movie, data = request.data)
#         except Movie.DoesNotExist:
#             return Response('Error', status=status.HTTP_404_NOT_FOUND)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data ,status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def delete(self, request, pk):
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response("data deleted successfully", status=status.HTTP_204_NO_CONTENT)


#################################################################

# @api_view(['GET', 'POST']) 
# def StreamPlatformListView(request):
#     if request.method == 'GET':
#         movies = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(movies, many=True)
#         return Response(serializer.data)
        
#     if request.method == 'POST':
#         serializer = StreamPlatformSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

# @api_view(['GET', 'PUT', 'DELETE'])
# def StreamPlatformDetailsView(request, pk):

#     if request.method == 'GET':
#         movie = StreamPlatform.objects.get(pk=pk)
#         serializer = StreamPlatformSerializer(movie)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         movie = StreamPlatform.objects.get(pk=pk)
#         serializer = StreamPlatformSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return  Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        
#     if request.method == 'DELETE':
#         movie = StreamPlatform.objects.get(pk=pk)
#         movie.delete()
#         return Response('data deleted successfully', status=status.HTTP_404_NOT_FOUND)





# @api_view(['GET', 'POST'])
# def WatchListListView(request):

#     if request.method == 'GET':
#         movies = WatchList.objects.all()
#         serializer = WatchListSerializer(movies, many=True)
#         return Response(serializer.data)
        
#     if request.method == 'POST':
#         serializer = WatchListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

# @api_view(['GET', 'PUT', 'DELETE'])
# def WatchListDetailsView(request, pk):

#     if request.method == 'GET':
#         movie = WatchList.objects.get(pk=pk)
#         serializer = WatchListSerializer(movie)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         movie = WatchList.objects.get(pk=pk)
#         serializer = WatchListSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return  Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        
#     if request.method == 'DELETE':
#         movie = WatchList.objects.get(pk=pk)
#         movie.delete()
#         return Response('data deleted successfully', status=status.HTTP_404_NOT_FOUND)

##################################################


# class StreamPlatformListViewAv(APIView):


#     def get(self, request):
#         movies = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(movies, many=True) # , context = {'request': request}[for hyperlink]
#         return Response(serializer.data)
    
    
#     def post(self, request):
#         serializer = StreamPlatformSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

        

# class StreamPlatformDetailsViewAv(APIView):

#     def get(self, request, pk):
#         movie = StreamPlatform.objects.get(pk=pk)
#         serializer = StreamPlatformSerializer(movie) # context={'request': request}
#         return Response(serializer.data)

#     def put(self, request, pk):
#         movie = StreamPlatform.objects.get(pk=pk)
#         serializer = StreamPlatformSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        
#     def delete(self, request, pk):
#         movie = StreamPlatform.objects.get(pk=pk)
#         movie.delete()
#         return Response('data deleted successfully')



class WatchListViewAv(APIView):
    permission_classes  =[IsAuthenticatedOrReadOnly]  # if user is logged out, he can view movie list but he cannot access..
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)
class WatchlistCreateViewAv(APIView):

    permission_classes  =[IsAdminUser] 
    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class WatchListDetailsViewAv(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    def delete(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response('data deleted successfully')
    
# we are not writing the views, as we have written earlier using APIView or @api_view().
# we are using the [GENERIC VIEW] with [MIXINS].


# "using mixins"

# class ReviewListView(mixins.ListModelMixin, 
#                      mixins.CreateModelMixin,
#                      generics.GenericAPIView):
    
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
# class ReviewDetailViewAv(mixins.RetrieveModelMixin,
#                          mixins.UpdateModelMixin,
#                          mixins.DestroyModelMixin,
#                          generics.GenericAPIView):
    
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
    
# Now we are using the concrete generic class methods..

class ReviewListViewAv(generics.ListAPIView):

    # queryset = Review.objects.all()  i need only the review of a single movie , so removing query set and creating a function called query_set??
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]  # if user is not logged in he can not do any task..
    throttle_classes = [UserRateThrottle, AnonRateThrottle]  # user can access only the respected the time of rate that is defined in the settings..

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)

class ReviewsCreateViewAv(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Review.objects.all() # this function is to get the Review objects for the user..  
    
    
    def perform_create(self,serializer):

        pk = self.kwargs['pk']
        watchlist = WatchList.objects.get(pk=pk)

        # checking whether the user has already added review if added for a movie, he cannot add again
        
        current_user = self.request.user
        reviewed_queryset = Review.objects.filter(watchlist=watchlist, review_user = current_user) 

        # if user has already given review, then he will be inside the reviewed_queryset// 
        if reviewed_queryset.exists(): # if any data exists in queryset, means this is user also exists and given review already
            raise ValidationError('You have already Reviewed This movie, you cannot do it again, please update if u need')

        if watchlist.total_ratings == 0:
            watchlist.avr_rating = serializer.validated_data['rating']
        else:
            watchlist.avr_rating = (watchlist.avr_rating + serializer.validated_data['rating']) / 2
        
        watchlist.total_ratings = watchlist.total_ratings + 1
        watchlist.save()


        serializer.save(watchlist = watchlist, review_user = current_user) 
        # we need to pass both movielist and user if user is not added review..


    
    # here we are getting the id of every movie of a single stream platform and we are storing the reviews of the single movie..
    # once we get the primary key, we are accessing the movie/watchlist from the primary key, 
    # saving the movie review inside the respected movie..



class ReviewDetailViewAv(generics.RetrieveUpdateDestroyAPIView):

    queryset = Review.objects.all()  
    # ? getting all the data from Reviews. 
    serializer_class = ReviewSerializer

    permission_classes = [ReviewUserOrReadonly]
    # ? only the respected user can edit the review an others can view the review.

    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    # ?  # user can access only the respected the time of rate that is defined in the settings..

    

# trying to write the StreamPlatformView using views.Viewset()

# class StreamPlatformViewVS(viewsets.ViewSet):

#     def list(self, request): # GET
#         queryset = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(queryset, many=True)
#         return Response(serializer.data)
    
#     def retrieve(self, request, pk=None): # GET BY PK
#         queryset = StreamPlatform.objects.all()
#         watchlist = get_object_or_404(queryset, pk=pk)
#         serializer = StreamPlatformSerializer(watchlist)
#         return Response(serializer.data)

    
#     def create(self, request): # POST
#         serializer = StreamPlatformSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
#     def update(self,request, pk=None):
#         queryset = StreamPlatform.objects.all()
#         watchlist = get_object_or_404(queryset, pk=pk)
#         serializer = StreamPlatformSerializer(watchlist, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
    
#     def destroy(self, request, pk=None):
#         queryset = StreamPlatform.objects.all()
#         watchlist = get_object_or_404(queryset, pk=pk)
#         watchlist.delete()
#         return Response(f'{watchlist} Platform deleted successfully',status=status.HTTP_204_NO_CONTENT)
    

# creating a views using the ModelViewSet which contains all the set of [List, Retrieve, Destroy, Update,Create] functions inside it...
class StreamPlatformViewVS(viewsets.ModelViewSet):
    
    permission_classes = [IsAdminUser]
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer 
    