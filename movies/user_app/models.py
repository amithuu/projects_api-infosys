import uuid
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
from user_app.api.validators import CustomLengthValidator
from django.contrib.auth.models import User
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
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
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
    
    # supplemental_pay =  models.CharField(max_length=255, validators=[CustomLengthValidator(min_length=2, max_length=255, field_name= 'supplemental_pay')])
    benefits = models.CharField(max_length=255, validators=[CustomLengthValidator(min_length=8, max_length=255, field_name= 'benefits')])
    
    # * Notice Period==================================
    notice_period = models.IntegerField(validators=[CustomLengthValidator(min_value=1, max_value=50, field_name= 'notice_period')])
    blind_hire = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.job_title + ' ' + str(self.id)

Days_Choice = [
    ('Monday-Friday', 'monday-friday'),
    ('Monday-Saturday', 'monday-saturday'), 
    ('Flexible', 'flexible'),
]

SKILL_LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'), 
        ('advanced','Advanced'),   
    ]
Extra_PAY_Choice =[
    ('Performance Bonus', 'performance bonus'),
    ('Yearly Bonus', 'yearly bonus'),
    ('Quarterly Bonus', 'quarterly bonus'), 
    ('Commission', 'commission'), 
    ('Overtime Pay', 'overtime pay'),  
    ('Shift Allowance', 'shift allowance'), 
    ('Joining Bonus', 'joining bonus'), 
    ('ESOP', 'esop'),    
]


class Job_Post(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default = uuid.uuid4)
    created_on = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255, validators=[CustomLengthValidator(min_length=2, max_length=255, field_name='job_title')])
    management_level = models.CharField(max_length=255, validators=[CustomLengthValidator(min_length=2, max_length=255, field_name='management_level')])
    job_type = models.CharField(max_length=255, validators=[CustomLengthValidator(min_length=2, max_length=255, field_name='job_type')])
    no_of_openings = models.IntegerField(validators=[CustomLengthValidator(min_length=1, max_length=50, field_name='no_og_openings')])
    days = models.CharField(max_length=17 ,choices=Days_Choice)
    specific_timing = models.BooleanField()
    specific_time = models.TimeField()
    flexible_timing = models.BooleanField()
    flexible_time = models.TimeField()
    minimum_years_experience = models.IntegerField(validators=[CustomLengthValidator(min_value=1, max_value=49, field_name= 'minimum_years_experience')])
    maximum_years_experience = models.IntegerField(validators=[CustomLengthValidator(min_value=1, max_value=49, field_name= 'maximum_years_experience')])
    roles_responsibility = models.TextField(max_length=255, validators=[CustomLengthValidator(min_length=8, max_length=255, field_name= 'roles_responsibility')])
    minimum_pay = models.IntegerField(validators=[CustomLengthValidator(min_value=1, max_value=100000, field_name= 'minimum_pay')])
    maximum_pay = models.IntegerField(validators=[CustomLengthValidator(min_value=1, max_value=100000, field_name= 'maximum_pay')])
    notice_period = models.IntegerField(validators=[CustomLengthValidator(min_value=1, max_value=1000, field_name= 'notice_period')])
    blind_hire = models.BooleanField(default=False)    
    
    def __str__(self):
        return self.job_title + ' ' + str(self.id) + ' ' + str(self.creator)
    
# ! location as array
class Location(models.Model):
    location = models.CharField(max_length=255)
    remote_job = models.BooleanField()
    job_post = models.ForeignKey(Job_Post, on_delete=models.CASCADE, related_name= 'locations')
    
    def __str__(self):
        return self.location
    
class HardSkill(models.Model):
    hard_skill = models.CharField(max_length=255, validators=[CustomLengthValidator(min_length=1, max_length=255, field_name='hards_kill')])
    deal_breaker = models.BooleanField(default=False)
    hard_skill_expertise = models.IntegerField(validators=[CustomLengthValidator(min_value=1, max_value=10, field_name = 'hard_skill_expertise')])
    job_post = models.ForeignKey(Job_Post, on_delete=models.CASCADE, related_name = 'hard_skills')
    
    def __str__(self):
        return self.hard_skill
    
class SoftSkill(models.Model):
    soft_skill = models.CharField(max_length = 255, validators=[CustomLengthValidator(min_length=2, max_length=255, field_name= 'soft_skill')])
    soft_skill_expertise  = models.IntegerField(validators=[CustomLengthValidator(min_value=1, max_value=10, field_name= 'soft_skill_expertise')])
    job_post = models.ForeignKey(Job_Post, on_delete=models.CASCADE, related_name = 'soft_skills')
    
    
    def __str__(self):
        return self.soft_skill
    

class Language(models.Model):
    language = models.CharField(max_length=255, validators=[CustomLengthValidator(min_length=2, max_length=255, field_name= 'language')])
    language_expertise = models.CharField(max_length=15 ,choices = SKILL_LEVEL_CHOICES )
    deal_breaker = models.BooleanField(default = False)
    job_post = models.ForeignKey(Job_Post, on_delete=models.CASCADE, related_name='languages')
    
    def __str__(self):
        return self.language
    

class IndustryExperience(models.Model):
    industry = models.CharField(max_length=255, validators=[CustomLengthValidator(min_length=2, max_length=255, field_name= 'industry')])
    minimum_industry_experience = models.IntegerField(validators=[CustomLengthValidator(min_value=1, max_value=49, field_name= 'minimum_industry_experience')])
    job_post = models.ForeignKey(Job_Post, on_delete=models.CASCADE, related_name = 'industrys')
    
    def __str__(self):
        return self.industry
    
class CompanyExperience(models.Model):
    company = models.CharField(max_length=255, validators=[CustomLengthValidator(min_length=2, max_length=255, field_name= 'company')])
    minimum_company_experience = models.IntegerField(validators=[CustomLengthValidator(min_value=1, max_value=49, field_name= 'minimum_company_experience')])
    job_post = models.ForeignKey(Job_Post, on_delete=models.CASCADE, related_name = 'companys')
    
    def __str__(self):
        return self.company
    
class Benefits(models.Model):
    benefit = models.CharField(max_length=255, choices= Extra_PAY_Choice, validators=[CustomLengthValidator(min_length=1, max_length=255, field_name= 'benefit')],)
    job_post = models.ForeignKey(Job_Post, on_delete=models.CASCADE, related_name= 'benefits')
    
    def __str__(self):
        return self.benefit
    
class SupplementPay(models.Model):
    supplement_pay = models.CharField(max_length=255, choices= Extra_PAY_Choice, validators=[CustomLengthValidator(min_length=1, max_length=255, field_name= 'supplement_pay')], )
    job_post = models.ForeignKey(Job_Post, on_delete=models.CASCADE, related_name= 'supplement_pays')
    
    def __str__(self):
        return self.supplement_pay
    
    
    
 