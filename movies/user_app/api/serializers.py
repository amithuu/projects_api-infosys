# from user_app.models import Register
from django.contrib.auth.models import User 
# ! here we are using User Model which gives [username, email,password] by default
from rest_framework import serializers
from user_app.models import JobPost, Job_Post, HardSkill, SoftSkill, IndustryExperience, CompanyExperience, Location, Language, Benefits, SupplementPay

class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type':'password'},write_only=True)
# * this is extra fields we are adding instead of User Model attribute

    class Meta:
        model = User
        fields = ['username', 'email', 'password','confirm_password']
        extra_kwargs = {
            'password':{'write_only':True}
        }        

    def save(self):

        password = self.validated_data['password'] # ! if we need any current value to store from the post request, we user validate_data['field_name']
        confirm_password = self.validated_data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError({'Error':'Password and confirm_password should be same'})
        
        user = User.objects.filter(email = self.validated_data['email'])
        if user.exists():
            raise serializers.ValidationError({'Error':'Email already exits'})

        user = User(email=self.validated_data['email'], username = self.validated_data['username'])
        user.set_password(password)
        user.save()
        return user
    
        # * we are overriding the save() method by checking the validations, else we get error as ,
        # ! Got a `TypeError` when calling `User.objects.create()`. [AS WE ARE DOING SOME EXTRA CHANGES THOSE ARE NOT SAVING IN DEFAULT DATABASE, SO WE NEED TO OVERRIDE THE SAVE() METHOD]
        # ! This may be because you have a writable field on the serializer class that is not a valid argument to `User.objects.create()`. 
        # ! You may need to make the field read-only, or override the RegisterSerializer.create() method to handle this correctly.
        

class JobPostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = JobPost
        fields = "__all__"
    

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['location', 'remote_job',]  

class HardSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = HardSkill
        fields = ['hard_skill', 'deal_breaker', 'hard_skill_expertise',]
        
class SoftSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoftSkill
        fields = ['soft_skill', 'soft_skill_expertise',]
        
class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['language', 'language_expertise', 'deal_breaker',]
        
        
class IndustryExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndustryExperience
        fields = ['industry', 'minimum_industry_experience',]
        
class CompanyExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyExperience
        fields = ['company', 'minimum_company_experience',]
        
class BenefitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefits
        fields = ['benefit',]

class SupplementPaySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SupplementPay
        fields = ['supplement_pay',]    
        
class Job_PostSerializer(serializers.ModelSerializer):
    locations = LocationSerializer(many=True)
    hard_skills = HardSkillSerializer(many=True)
    soft_skills = SoftSkillSerializer(many=True)
    languages = LanguageSerializer(many=True)
    industrys = IndustryExperienceSerializer(many=True)
    companys = CompanyExperienceSerializer(many=True)
    benefits = BenefitsSerializer(many=True)
    supplement_pays = SupplementPaySerializer(many=True)
    
    class Meta:
        model = Job_Post
        fields = [
            'id', 'created_on', 'creator', 'job_title', 'management_level', 'job_type',
            'no_of_openings', 'days', 'specific_timing', 'specific_time', 'flexible_timing',
            'flexible_time', 'minimum_years_experience', 'maximum_years_experience',
            'roles_responsibility', 'minimum_pay', 'maximum_pay',
            'notice_period', 'blind_hire', 'locations', 'hard_skills',
            'soft_skills', 'languages', 'industrys', 'companys', 'benefits', 'supplement_pays',
        ]
        extra_kwargs = {
            'creator': {'read_only': True},
        }

    def create(self, validated_data):
        locations_data = validated_data.pop('locations')
        hard_skills_data = validated_data.pop('hard_skills')
        soft_skills_data = validated_data.pop('soft_skills')
        languages_data = validated_data.pop('languages')
        industrys_data = validated_data.pop('industrys')
        companys_data = validated_data.pop('companys')
        benefits_data = validated_data.pop('benefits')
        supplement_pays_data = validated_data.pop('supplement_pays')

        job_post = Job_Post.objects.create(**validated_data)

        for location_data in locations_data:
            Location.objects.create(job_post=job_post, **location_data)

        for hard_skill_data in hard_skills_data:
            HardSkill.objects.create(job_post=job_post, **hard_skill_data)

        for soft_skill_data in soft_skills_data:
            SoftSkill.objects.create(job_post=job_post, **soft_skill_data)

        for language_data in languages_data:
            Language.objects.create(job_post=job_post, **language_data)

        for industry_data in industrys_data:
            IndustryExperience.objects.create(job_post=job_post, **industry_data)

        for company_data in companys_data:
            CompanyExperience.objects.create(job_post=job_post, **company_data)

        for benefit_data in benefits_data:
            Benefits.objects.create(job_post=job_post, **benefit_data)

        for supplement_pay_data in supplement_pays_data:
            SupplementPay.objects.create(job_post=job_post, **supplement_pay_data)

        return job_post
    
    
    def update(self, instance, validated_data):
        locations_data = validated_data.pop('locations', [])
        hard_skills_data = validated_data.pop('hard_skills', [])
        soft_skills_data = validated_data.pop('soft_skills', [])
        languages_data = validated_data.pop('languages', [])
        industrys_data = validated_data.pop('industrys', [])
        companys_data = validated_data.pop('companys', [])
        benefits_data = validated_data.pop('benefits', [])
        supplement_pays_data = validated_data.pop('supplement_pays', [])

        instance = super().update(instance, validated_data)

        for location_data in locations_data:
            Location.objects.create(job_post=instance, **location_data)

        for hard_skill_data in hard_skills_data:
            HardSkill.objects.create(job_post=instance, **hard_skill_data)

        for soft_skill_data in soft_skills_data:
            SoftSkill.objects.create(job_post=instance, **soft_skill_data)

        for language_data in languages_data:
            Language.objects.create(job_post=instance, **language_data)

        for industry_data in industrys_data:
            IndustryExperience.objects.create(job_post=instance, **industry_data)

        for company_data in companys_data:
            CompanyExperience.objects.create(job_post=instance, **company_data)

        for benefit_data in benefits_data:
            Benefits.objects.create(job_post=instance, **benefit_data)

        for supplement_pay_data in supplement_pays_data:
            SupplementPay.objects.create(job_post=instance, **supplement_pay_data)

        return instance
    
    def destroy(self, instance):
        instance.delete()