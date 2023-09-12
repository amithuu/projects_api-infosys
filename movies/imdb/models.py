from django.db import models

# Create your models here.


class StreamPlatform(models.Model):
    platform_name = models.CharField(max_length=30)
    about_platform = models.CharField(max_length=150)
    website_link = models.URLField(max_length=100)

    def __str__(self):
        return self.platform_name
    
    
class WatchList(models.Model):
    movie_name = models.CharField(max_length=20)
    movie_desc = models.CharField(max_length=150)
    platform = models.ForeignKey(StreamPlatform,on_delete=models.CASCADE, related_name='watchlist')
    movie_status = models.BooleanField(default=True)
    movie_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.movie_name
    
# ? platform = models.ForeignKey(StreamPlatform,on_delete=models.CASCADE, related_name='watchlist')

# ? the above line is to add the relations from Stream to WatchList..[which is one  to one relation][one movie can have only one platform]


