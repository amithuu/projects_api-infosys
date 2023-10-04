import uuid
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
from user_app.api.validators import CustomLengthValidator
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


SKILL_LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]


class JobPost(models.Model):
    #* Basic details page=======================================
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job_title = models.CharField(max_length=255, validators=[CustomLengthValidator(min_length=2, max_length=255, field_name='job_title')])
    functional_area = models.CharField(max_length=255, validators=[CustomLengthValidator(min_length=2, max_length=255, field_name='functional_area')])
    management_level = models.CharField(max_length=255, validators=[CustomLengthValidator(min_length=2, max_length=255, field_name='management_level')])
    no_of_openings = models.IntegerField(validators=[CustomLengthValidator(min_value=1, max_value=50, field_name='no_of_openings')])
    job_type = models.CharField(max_length=255, validators=[CustomLengthValidator(min_length=2, max_length=255, field_name='job_type')])
    location = models.CharField(max_length=255, validators=[CustomLengthValidator(min_length=8, max_length=255, field_name='location')])
    remote_job = models.BooleanField()
    specific_timing = models.BooleanField(default=False)
    specific_time = models.TimeField(null=True, blank=True)
    flexible_timing = models.BooleanField(default=False)
    flexible_time = models.TimeField(null=True, blank=True)
    
    #* Skills page============================================
    
    #? hard skills
    hard_skill = models.CharField(max_length=255, validators=[CustomLengthValidator(min_length=2, max_length=255, field_name='hard_skill')])
    hard_kill_expertise_level = models.IntegerField(validators=[CustomLengthValidator(min_value=1, max_value=10, field_name="hard_kill_expertise_level")]) 
    deal_breaker_hard_skill = models.BooleanField(default=False)
    
    #? Soft skill
    soft_skills = models.CharField(max_length=255, validators=[CustomLengthValidator(min_length=2, max_length=255, field_name="soft_skills")])
    soft_skill_expertise_level = models.IntegerField(validators=[CustomLengthValidator(min_value=1, max_value=10, field_name="soft_skill_expertise_level")])
    
    #? languages 
    language = models.CharField(max_length=255, validators=[CustomLengthValidator(min_length=2, max_length=255, field_name= 'language')])
    language_expertise_level = models.IntegerField(validators=[CustomLengthValidator(min_value=1, max_value=10, field_name= 'language_expertise_level')])
    deal_breaker_language = models.BooleanField(default=False)
    
    # * Experience==========================================
    
    # ? overall experience
    min_years_experience = models.IntegerField(validators=[CustomLengthValidator(min_value=1, max_value=50, field_name= 'min_years_experience')])
    
    max_years_experience = models.IntegerField(validators=[CustomLengthValidator(min_value=1, max_value=50, field_name= 'max_years_experience')])
    
    include_fresher = models.BooleanField(default=False)
    
    # ? industry Experience 
    industry_experience = models.CharField(max_length=255, validators=[CustomLengthValidator(min_length=3, max_length=255, field_name= 'industry_experience')])
    min_years_industry_experience = models.IntegerField(validators=[CustomLengthValidator(min_value=1, max_value=50, field_name= 'min_years_industry_experience')])
    max_years_industry_experience = models.IntegerField(validators=[CustomLengthValidator(min_value=1, max_value=50, field_name= 'max_years_industry_experience')])
    
    # ? company experience
    company_experience = models.CharField(max_length=255, validators=[CustomLengthValidator(min_length=8, max_length=255, field_name= 'company_experience')])
    min_years_company_experience = models.IntegerField(validators=[CustomLengthValidator(min_value=1, max_value=50, field_name= 'min_years_company_experience')])

    # ! education level field will be adding in the future///  

    # * Roles and Responsibility===================================
    roles_responsibility = models.TextField(validators=[CustomLengthValidator(min_length=10, max_length=255, field_name= 'roles_responsibility')])
    
    
    # * Pay and Benefits================================
    # ? Minimum salary max pay scale
    #! dollar symbol and rupees Symbol field need to be added
    min_pay_salary = models.IntegerField(validators=[CustomLengthValidator(min_value=1, max_value=500000000000,field_name= 'min_pay_salary')])
    max_pay_salary = models.IntegerField(validators=[CustomLengthValidator(min_value=1, max_value=500000000000, field_name= 'max_pay_salary')])
    
    supplemental_pay =  models.CharField(max_length=255, validators=[CustomLengthValidator(min_length=2, max_length=255, field_name= 'supplemental_pay')])
    benefits = models.CharField(max_length=255, validators=[CustomLengthValidator(min_length=8, max_length=255, field_name= 'benefits')])
    
    # * Notice Period==================================
    notice_period = models.IntegerField(validators=[CustomLengthValidator(min_value=1, max_value=50, field_name= 'notice_period')])
    blind_hire = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.job_title + ' ' + str(self.id)
    
    