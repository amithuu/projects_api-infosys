from imdb.models import WatchList, StreamPlatform, Review
from imdb.api.serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins

# @api_view()
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

class StreamPlatformListViewAv(APIView):


    def get(self, request):
        movies = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(movies, many=True) # , context = {'request': request}[for hyperlink]
        return Response(serializer.data)
    
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class StreamPlatformDetailsViewAv(APIView):

    def get(self, request, pk):
        movie = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(movie) # context={'request': request}
        return Response(serializer.data)

    def put(self, request, pk):
        movie = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    def delete(self, request, pk):
        movie = StreamPlatform.objects.get(pk=pk)
        movie.delete()
        return Response('data deleted successfully')



class WatchListViewAv(APIView):
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class WatchListDetailsViewAv(APIView):
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

class ReviewListView(mixins.ListModelMixin, 
                     mixins.CreateModelMixin,
                     generics.GenericAPIView):
    
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    
    









    
