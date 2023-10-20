from django.contrib import admin
from .models import WatchList, StreamPlatform, Review
from user_app.models import JobPost, JobPostLocation, JobPostHardSkill, JobPostSoftSkill, JobPostLanguage, JobPostIndustryExperience, JobPostCompanyExperience,JobPostOverallExperience, JobPostBenefits, JobPostSupplementPay, Onboarding, OnboardingBranches

# Register your models here.

# admin.site.register(WatchList)
admin.site.register(StreamPlatform)
admin.site.register(Review)
admin.site.register(JobPost)
admin.site.register(JobPostLocation)
admin.site.register(JobPostHardSkill)
admin.site.register(JobPostSoftSkill)
admin.site.register(JobPostLanguage)
admin.site.register(JobPostIndustryExperience)
admin.site.register(JobPostCompanyExperience)
admin.site.register(JobPostOverallExperience)
admin.site.register(JobPostBenefits)
admin.site.register(JobPostSupplementPay)
admin.site.register(Onboarding)
admin.site.register(OnboardingBranches)




@admin.register(WatchList)
class CustomWatchlist(admin.ModelAdmin):
    list_display = ('movie_name', 'platform', 'total_ratings')
    ordering = ('movie_created', )
    search_fields = ('movie_name', 'movie_created',)
    list_filter = ('movie_name', 'platform', 'total_ratings',)
