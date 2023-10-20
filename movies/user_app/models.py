import uuid
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
from user_app.api.validators import CustomLengthValidator
from django.contrib.auth.models import User
from config.constants import DAYS_CHOICE, SKILL_LEVEL_CHOICES, SUPPLEMENT_PAY_CHOICES, SCALE_OF_COMPANY
# from timestamps.models import models, Timestampable, SoftDeletes  


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

class JobPost(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default = uuid.uuid4)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, validators=[CustomLengthValidator(min_length=2, max_length=255, field_name='title')])
    description = models.TextField(null=True)
    functional_area = models.CharField(null=True, max_length=255, validators=[CustomLengthValidator(min_length=2, max_length=255, field_name='functional_area')])
    management_level = models.CharField(null=True, max_length=255, validators=[CustomLengthValidator(min_length=2, max_length=255, field_name='management_level')])
    job_type = models.CharField(null=True, max_length=255, validators=[CustomLengthValidator(min_length=2, max_length=255, field_name='job_type')])
    opening_slots = models.IntegerField(default=0, validators=[CustomLengthValidator(min_length=1, max_length=50, field_name='opening_slots')])
    is_remote = models.BooleanField(default=False)  
    schedule_days = models.CharField(null=True, max_length=30 ,choices=DAYS_CHOICE)
    specific_timing = models.BooleanField(default=False)
    start_specific_time = models.TimeField(null=True)
    end_specific_time = models.TimeField(null=True)
    flexible_timing = models.BooleanField(default=False)
    flexible_time = models.TimeField(null=True)
    min_years_experience = models.IntegerField(null=True, validators=[CustomLengthValidator(min_value=1, max_value=49, field_name= 'min_years_experience')])
    max_years_experience = models.IntegerField(null=True, validators=[CustomLengthValidator(min_value=1, max_value=49, field_name= 'max_years_experience')])
    education_level = models.CharField(null=True, max_length=30) 
    include_freshers = models.BooleanField(default=False) 
    roles_responsibilities = models.TextField(null=True, max_length=255, validators=[CustomLengthValidator(min_length=8, max_length=255, field_name= 'roles_responsibilities')])
    pay_currency = models.CharField(null=True, max_length=4)
    min_pay = models.CharField(null=True, max_length=255, validators=[CustomLengthValidator(min_length=1, max_length=256, field_name= 'min_pay')])
    max_pay = models.CharField(null=True, max_length=255, validators=[CustomLengthValidator(min_length=1, max_length=256, field_name= 'max_pay')]) 
    notice_period = models.IntegerField(validators=[CustomLengthValidator(min_value=1, max_value=1000, field_name= 'notice_period')])
    blind_hire = models.BooleanField(default=False)    
    hiring_status = models.CharField(null=True, max_length=30)
    rejected_ids = models.JSONField(blank=True, null=True)  
    Company = models.UUIDField(blank=True, null=True) #! LATER DOING AS FOREIGN KEY
     
    def __str__(self):
        return self.title + ' ' + str(self.id) + ' ' + str(self.creator)


  
# ! location as array[building separate models because we are taking them in a list of input  soo..]
# ? [When ever we create an model for string the array elements , 
# ? the validation wont happen for every element , 
# ? for we need to create explicitly a Create() function to validate it, similarly for Update() and Delete() as well "@ serializer.py"]
# * and we use a variable[ex:job_post] to build the relationship between the elements and the Job_Post model 

class JobPostLocation(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default = uuid.uuid4)
    location = models.CharField(null=True, max_length=255)
    city = models.CharField(null=True, max_length=255)
    state = models.CharField(null=True, max_length=255)
    country = models.BooleanField(null=True)
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE, related_name='job_post_locations')
    
    class Meta:
        db_table = "job_post_locations"
        
    def __str__(self):
        return self.location


class JobPostHardSkill(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default = uuid.uuid4)
    name = models.CharField(null=True, max_length=255, validators=[CustomLengthValidator(min_length=1, max_length=255, field_name='name')])
    deal_breaker = models.BooleanField(null=True,default=False)
    expertise = models.IntegerField(null=True,validators=[CustomLengthValidator(min_value=1, max_value=10, field_name = 'expertise')])
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE, related_name = 'job_post_hard_skills')
    
    class Meta:
        db_table = "job_post_hard_skills"
        
    def __str__(self):
        return self.name
    
class JobPostSoftSkill(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default = uuid.uuid4)
    name = models.CharField(null=True,max_length = 255, validators=[CustomLengthValidator(min_length=2, max_length=255, field_name= 'name')])
    expertise  = models.IntegerField(null=True,validators=[CustomLengthValidator(min_value=1, max_value=10, field_name= 'expertise')])
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE, related_name = 'job_post_soft_skills')
    
    class Meta:
        db_table = "job_post_soft_skills"
    
    def __str__(self):
        return self.name
    

class JobPostLanguage(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default = uuid.uuid4)
    name = models.CharField(null=True,max_length=255, validators=[CustomLengthValidator(min_length=2, max_length=255, field_name= 'name')])
    expertise = models.CharField(null=True,max_length=15 ,choices = SKILL_LEVEL_CHOICES )
    deal_breaker = models.BooleanField(null=True,default = False)
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE, related_name='job_post_languages')
    
    class Meta:
        db_table = "job_post_languages"
        
    def __str__(self):
        return self.name
    

class JobPostIndustryExperience(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default = uuid.uuid4)
    name = models.CharField(null=True,max_length=255, validators=[CustomLengthValidator(min_length=2, max_length=255, field_name= 'name')])
    min_experience = models.IntegerField(null=True,validators=[CustomLengthValidator(min_value=1, max_value=49, field_name= 'min_experience')])
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE, related_name = 'job_post_industry_experiences')
    
    class Meta:
        db_table = "job_post_industry_experiences"
        
    def __str__(self):
        return self.name
    
class JobPostCompanyExperience(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default = uuid.uuid4)
    name = models.CharField(null=True,max_length=255, validators=[CustomLengthValidator(min_length=2, max_length=255, field_name= 'name')])
    min_experience = models.IntegerField(null=True,validators=[CustomLengthValidator(min_value=1, max_value=49, field_name= 'min_experience')])
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE, related_name = 'job_post_company_experiences')
    
    class Meta:
        db_table = "job_post_company_experiences"
        
    def __str__(self):
        return self.name

class JobPostOverallExperience(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default = uuid.uuid4)
    min_experience = models.DateField(null=True)
    max_experience = models.DateField(null=True)
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE, related_name = 'job_post_overall_experiences')
    
    class Meta:
        db_table = "job_post_overall_experiences"
        
    def __str__(self):
        return str(self.min_experience)
    
class JobPostBenefits(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default = uuid.uuid4)
    name = models.CharField(null=True,max_length=255, choices= SUPPLEMENT_PAY_CHOICES, validators=[CustomLengthValidator(min_length=1, max_length=255, field_name= 'name')])
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE, related_name= 'job_post_benefits')
    
    class Meta:
        db_table = "job_post_benefits"
        
    def __str__(self):
        return self.name
    
class JobPostSupplementPay(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default = uuid.uuid4)
    name = models.CharField(null=True,max_length=255, choices= SUPPLEMENT_PAY_CHOICES, validators=[CustomLengthValidator(min_length=1, max_length=255, field_name= 'amount')] )
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE, related_name= 'job_post_supplement_pays')
    
    class Meta:
        db_table = "job_post_supplement_pays"
        
    def __str__(self):
        return self.name
   


                                                    #?###############ONBOARDING#####################
     
   
class Onboarding(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    onboarding_company_name = models.CharField(max_length=255, validators=[CustomLengthValidator(min_length=1, max_length=255, field_name = 'company_name')])
    onboarding_industry = models.CharField(max_length=255, validators=[CustomLengthValidator(min_length=1, max_length=255, field_name = 'company_industry')])
    onboarding_scale = models.CharField(max_length=255,choices = SCALE_OF_COMPANY,  validators=[CustomLengthValidator(min_length=1, max_length=255, field_name = 'company_scale')]) 
    total_employees = models.IntegerField(validators=[CustomLengthValidator(min_value = 1, max_value = 500, field_name = 'total_employees')])
    
    onboarding_company_vision = models.TextField(max_length=255, validators=[CustomLengthValidator(min_length = 1, max_length =255, field_name ='company_vision')])
    onboarding_company_values = models.TextField(max_length=255, validators=[CustomLengthValidator(min_length = 1, max_length =255, field_name ='company_values')])
    onboarding_company_culture = models.TextField(max_length=255, validators=[CustomLengthValidator(min_length = 1, max_length =255, field_name ='company_culture')])

    onboarding_linkedin = models.URLField(max_length = 128, unique=True, validators=[CustomLengthValidator(min_length = 1, max_length= 128, field_name = 'linkedin')])
    onboarding_website = models.URLField(max_length = 128, validators=[CustomLengthValidator(min_length=1, max_length = 128, field_name = 'website')])
    
    onboarding_pan = models.CharField(max_length = 256, validators=[CustomLengthValidator(min_length = 1, max_length = 256, field_name = 'pan')])
    onboarding_gst = models.CharField(max_length = 256, validators=[CustomLengthValidator(min_length = 1, max_length = 256, field_name = 'gst')])
    
    
    onboarding_headquarter = models.CharField(max_length = 256, validators=[CustomLengthValidator(min_length=1, max_length=256, field_name = 'headquarter')])
    onboarding_have_branches = models.BooleanField(default=False)
    
    # class Meta:
    #     db_table = 'onboardings'
        
    def __str__(self):
        return self.onboarding_company_name
    

class OnboardingBranches(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    onboarding_branches = models.CharField(max_length=255, validators=[CustomLengthValidator(min_length=2, max_length=255, field_name= 'branch')])
    onboarding = models.ForeignKey(Onboarding, on_delete=models.CASCADE,related_name = 'branches')
        
    def __str__(self):
        return self.onboarding_branches  
#################################################################################################
    
    