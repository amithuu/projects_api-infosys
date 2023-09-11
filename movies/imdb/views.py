# from django.shortcuts import render
# from .models import Movie
# from django.http import JsonResponse
# from django.views.generic import ListView
# # Create your views here.

# class MovieListView(ListView):
#     model = Movie
#     # template_name =

# def movie_list(request):
#     movie_list = Movie.objects.all()

#     data ={
#         'movie':list(movie_list.values())
#     }
#     return JsonResponse(data)

# def each_movie_list(request, pk):
#     movie_list = Movie.objects.get(pk=pk)
#     each_data = {
#         'name':movie_list.movie_name,
#         'description':movie_list.movie_desc,
#         'status': movie_list.movie_status
#     }

#     return JsonResponse(each_data)

