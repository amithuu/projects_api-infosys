from django.contrib import admin
from .models import WatchList, StreamPlatform, Review
from user_app.models import JobPost
# Register your models here.

# admin.site.register(WatchList)
admin.site.register(StreamPlatform)
admin.site.register(Review)
admin.site.register(JobPost)


@admin.register(WatchList)
class CustomWatchlist(admin.ModelAdmin):
    list_display = ('movie_name', 'platform', 'total_ratings')
    ordering = ('movie_created', )
    search_fields = ('movie_name', 'movie_created',)
    list_filter = ('movie_name', 'platform', 'total_ratings',)
