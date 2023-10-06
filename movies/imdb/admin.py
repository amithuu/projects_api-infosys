from django.contrib import admin
from .models import WatchList, StreamPlatform, Review
from user_app.models import JobPost, Job_Post, HardSkill, SoftSkill, Location, Language, IndustryExperience, CompanyExperience, Benefits, SupplementPay
# Register your models here.

# admin.site.register(WatchList)
admin.site.register(StreamPlatform)
admin.site.register(Review)
admin.site.register(JobPost)
admin.site.register(Job_Post)
admin.site.register(Location)
admin.site.register(HardSkill)
admin.site.register(SoftSkill)
admin.site.register(Language)
admin.site.register(IndustryExperience)
admin.site.register(CompanyExperience)
admin.site.register(Benefits)
admin.site.register(SupplementPay)




@admin.register(WatchList)
class CustomWatchlist(admin.ModelAdmin):
    list_display = ('movie_name', 'platform', 'total_ratings')
    ordering = ('movie_created', )
    search_fields = ('movie_name', 'movie_created',)
    list_filter = ('movie_name', 'platform', 'total_ratings',)
