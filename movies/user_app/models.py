from django.db import models

# Create your models here.
# class Register(models.Model):
#     firstname = models.CharField(max_length=10)
#     password = models.CharField(max_length=10)
#     email = models.EmailField(max_length=15)
#     confirm_password = models.CharField(max_length=10)

#     def __str__(self):
#         return self.email

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# ! the above model is used to create token for every user 



