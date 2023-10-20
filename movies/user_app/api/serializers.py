# from user_app.models import Register
from django.contrib.auth.models import User 
# ! here we are using User Model which gives [username, email,password] by default
from django.db.models import Q
from config.bulk_sync import bulk_sync
from config.functions import remove_item_from_list
from rest_framework import serializers
from user_app.models import JobPost, JobPostLocation, JobPostHardSkill, JobPostSoftSkill, \
    JobPostLanguage, JobPostIndustryExperience, JobPostCompanyExperience, JobPostOverallExperience, JobPostBenefits, \
    JobPostSupplementPay, Onboarding, OnboardingBranches
    
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
        

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPostLocation
        fields = ['id', 'location',]  


class HardSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPostHardSkill
        fields = ['id', 'name', 'deal_breaker', 'expertise',]
        

class SoftSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPostSoftSkill
        fields = ['id', 'name', 'expertise',]
        

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPostLanguage
        fields = ['id', 'name', 'expertise', 'deal_breaker',]
        
        
class IndustryExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPostIndustryExperience
        fields = ['id', 'name', 'min_experience',]
        
class CompanyExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPostCompanyExperience
        fields = ['id', 'name', 'min_experience',]

class OverallExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPostOverallExperience
        fields = ['id', 'min_experience', 'max_experience',]
        

class BenefitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPostBenefits
        fields = ['id', 'name',]


class SupplementPaySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPostSupplementPay
        fields = ['id', 'name',]   
        
        
        
           
        
class PostCreateSerializer(serializers.ModelSerializer):
    job_post_locations = LocationSerializer(many=True)
    job_post_hard_skills = HardSkillSerializer(many=True)
    job_post_soft_skills = SoftSkillSerializer(many=True)
    job_post_languages = LanguageSerializer(many=True)
    job_post_industry_experiences = IndustryExperienceSerializer(many=True)
    job_post_company_experiences = CompanyExperienceSerializer(many=True)
    job_post_overall_experiences = OverallExperienceSerializer(many=True)
    job_post_benefits = BenefitsSerializer(many=True)
    job_post_supplement_pays = SupplementPaySerializer(many=True)
    
    class Meta:
        model = JobPost
        fields = [
            'id','creator', 'title','description','functional_area','management_level', 'job_type',
            'opening_slots','is_remote','schedule_days', 'specific_timing', 'start_specific_time','end_specific_time','flexible_timing',
            'min_years_experience', 'max_years_experience','education_level','include_freshers',
            'roles_responsibilities','pay_currency','min_pay', 'max_pay',
            'notice_period', 'blind_hire','rejected_ids',
            'job_post_locations', 'job_post_hard_skills', 'job_post_soft_skills', 'job_post_languages', 'job_post_industry_experiences', 
            'job_post_company_experiences', 'job_post_overall_experiences', 'job_post_benefits', 'job_post_supplement_pays',
        ]
        extra_kwargs = {
            'creator': {'read_only': True},
        }
        
        
    # ? we need to create an create() to validate the data and post the job as it is array of objects/elements
    
    def create(self, validated_data):
        # ? {related_name_data} = {related_name}
        job_post_location_data = validated_data.pop('job_post_locations') # ! how this works, firstly it will get the data and it validates and pop's into the locations array of object
        job_post_hard_skill_data =  validated_data.pop('job_post_hard_skills')
        job_post_soft_skill_data = validated_data.pop('job_post_soft_skills')
        job_post_language_data= validated_data.pop('job_post_languages')
        job_post_industry_data = validated_data.pop('job_post_industries')
        job_post_company_data = validated_data.pop('job_post_companies')
        job_post_overall_data = validated_data.pop('job_post_overalls')
        job_post_benefit_data = validated_data.pop('job_post_benefits')
        job_post_supplement_pay_data = validated_data.pop('job_post_supplement_pays')
        
        job_post = JobPost.objects.create(**validated_data) # ! creating an instance to access the elements and create the data. and to validate all the fields inside the Job_Post Model..!!
        
        # ? this loop iterates through all the data received from the locations_data and checks validated and adds that to the job_post model..
        # ? modelname.objects.create(foreignkey=foreignkey, **data of the variable each validated)
        job_post_hard_skill_data =  validated_data.pop('job_post_hard_skills')
        job_post_soft_skill_data = validated_data.pop('job_post_soft_skills')
        job_post_language_data= validated_data.pop('job_post_languages')
        job_post_industry_data = validated_data.pop('job_post_industry_experiences')
        job_post_company_data = validated_data.pop('job_post_company_experiences')
        job_post_overall_data = validated_data.pop('job_post_overall_experiences')
        job_post_benefit_data = validated_data.pop('job_post_benefits')
        job_post_supplement_pay_data = validated_data.pop('job_post_supplement_pays') 
        
        
        locationsData = []
        for location_data in job_post_location_data:
            locationsData.append(JobPostLocation(job_post = job_post, **location_data))
            
        JobPostLocation.objects.bulk_create(locationsData)
        
        hardskillsData = []
        for hardskills_data in job_post_hard_skill_data:
            hardskillsData.append(JobPostHardSkill(job_post = job_post, **hardskills_data))
            
        JobPostHardSkill.objects.bulk_create(hardskillsData)
        
        
        softskillsData = []
        for softskills_data in job_post_soft_skill_data:
            softskillsData.append(JobPostSoftSkill(job_post = job_post, **softskills_data))
            
        JobPostSoftSkill.objects.bulk_create(softskillsData)
        
        languagesData = [] 
        for languages_data in job_post_language_data:
            languagesData.append(JobPostLanguage(job_post = job_post, **languages_data))
            
        JobPostLanguage.objects.bulk_create(languagesData)
        
        industriesData = []
        for industries_data in job_post_industry_data:
            industriesData.append(JobPostIndustryExperience(job_post = job_post, **industries_data))
            
        JobPostIndustryExperience.objects.bulk_create(industriesData)
        
        companiesData = []
        for companies_data in job_post_company_data:
            companiesData.append(JobPostCompanyExperience(job_post=job_post, **companies_data))
            
        JobPostCompanyExperience.objects.bulk_create(companiesData)

        overallsData = []
        for overalls_data in job_post_overall_data:
            overallsData.append(JobPostOverallExperience(job_post=job_post, **overalls_data))
            
        JobPostOverallExperience.objects.bulk_create(overallsData)

        benefitsData = []        
        for benefits_data in job_post_benefit_data:
            benefitsData.append(JobPostBenefits(job_post=job_post, **benefits_data))
            
        JobPostBenefits.objects.bulk_create(benefitsData)
        
        supplementPaysData = []
        for supplement_pays_data in job_post_supplement_pay_data:
            supplementPaysData.append(JobPostSupplementPay(job_post=job_post, **supplement_pays_data))
            
        JobPostSupplementPay.objects.bulk_create(supplementPaysData)
        
        return job_post 
        # ? at last we are returning all the data which is stored in job_post object..
    
    def validate_id(self, value):
        if not JobPost.objects.filter(creator=self.request.user, id=value).exits():
            raise serializers.ValidationError('Job not found')
        return value
    
    
    
class PostUpdateSerializer(serializers.ModelSerializer):
    job_post_locations = LocationSerializer(many=True)
    job_post_hard_skills = HardSkillSerializer(many=True)
    job_post_soft_skills = SoftSkillSerializer(many=True)
    job_post_languages = LanguageSerializer(many=True)
    job_post_industry_experiences = IndustryExperienceSerializer(many=True)
    job_post_company_experiences = CompanyExperienceSerializer(many=True)
    job_post_overall_experiences = OverallExperienceSerializer(many=True)
    job_post_benefits = BenefitsSerializer(many=True)
    job_post_supplement_pays = SupplementPaySerializer(many=True)
    
    class Meta:
        model = JobPost
        fields = [
            'id','creator', 'title','description','functional_area','management_level', 'job_type',
            'opening_slots','is_remote','schedule_days', 'specific_timing', 'start_specific_time','end_specific_time','flexible_timing',
            'min_years_experience', 'max_years_experience','education_level','include_freshers',
            'roles_responsibilities','pay_currency','min_pay', 'max_pay',
            'notice_period', 'blind_hire','rejected_ids',
            'job_post_locations', 'job_post_hard_skills', 'job_post_soft_skills', 'job_post_languages', 'job_post_industry_experiences', 
            'job_post_company_experiences', 'job_post_overall_experiences', 'job_post_benefits', 'job_post_supplement_pays',
        ]
        extra_kwargs = {
            'creator': {'read_only': True},
        }
       
    def update(self, instance, validated_data):
        job_post_location_data = validated_data.pop('job_post_locations', []) # ! how this works, firstly it will get the data and it validates and pop's into the locations array of object and empty list is to validated old and new data
        job_post_hard_skill_data =  validated_data.pop('job_post_hard_skills', [])
        job_post_soft_skill_data = validated_data.pop('job_post_soft_skills', [])
        job_post_language_data= validated_data.pop('job_post_languages', [])
        job_post_industry_data = validated_data.pop('job_post_industry_experiences', [])
        job_post_company_data = validated_data.pop('job_post_company_experiences', [])
        job_post_overall_data = validated_data.pop('job_post_overall_experiences', [])    
        job_post_benefit_data = validated_data.pop('job_post_benefits', [])
        job_post_supplement_pay_data = validated_data.pop('job_post_supplement_pays', [])    
        
        
        instance = super().update(instance, validated_data)  # ? we need old data and the new data        
        
        locationsData = []
        for location_data in job_post_location_data:
            locationsData.append(JobPostLocation(job_post = instance, **location_data))
            
        bulk_sync(
            new_models = locationsData,
            filters=Q(job_post=instance),
            fields = remove_item_from_list(key = 'id',list=LocationSerializer.Meta.fields),
            key_fields = ['location']
        )
        
        
        hardskillsData = []
        for hardskills_data in job_post_hard_skill_data:
            hardskillsData.append(JobPostHardSkill(job_post = instance, **hardskills_data))
            
        
        bulk_sync(
            new_models = hardskillsData,
            filters = Q(job_post = instance),
            fields = remove_item_from_list(key='id', list= HardSkillSerializer.Meta.fields),
            key_fields = ['deal_breaker', 'expertise',] 
        )
        
        
        softskillsData = []
        for softskills_data in job_post_soft_skill_data:
            softskillsData.append(JobPostSoftSkill(job_post = instance, **softskills_data))
            
        bulk_sync(
            new_models = softskillsData,
            filters = Q(job_post = instance),
            fields = remove_item_from_list(key='id', list =SoftSkillSerializer.Meta.fields),
            key_fields = ['name', 'expertise',]
            )
        
        languagesData = [] 
        for languages_data in job_post_language_data:
            languagesData.append(JobPostLanguage(job_post = instance, **languages_data))
            
        bulk_sync(
            new_models = languagesData,
            filters = Q(job_post = instance),
            fields = remove_item_from_list(key='id', list =LanguageSerializer.Meta.fields),
            key_fields = ['name', 'expertise','deal_breaker',]
        )
        
        industriesData = []
        for industries_data in job_post_industry_data:
            industriesData.append(JobPostIndustryExperience(job_post = instance, **industries_data))
            
        bulk_sync(
            new_models = industriesData,
            filters = Q(job_post = instance),
            fields = remove_item_from_list(key='id', list =IndustryExperienceSerializer.Meta.fields),
            key_fields = ['name', 'min_experience',]
        )
        
        
        companiesData = []
        for companies_data in job_post_company_data:
            companiesData.append(JobPostCompanyExperience(job_post=instance, **companies_data))   
        
        bulk_sync(
            new_models = companiesData,
            filters = Q(job_post = instance),
            fields = remove_item_from_list(key='id', list =CompanyExperienceSerializer.Meta.fields),
            key_fields = ['name', 'min_experience',]
        )

        overallsData = []
        for overalls_data in job_post_overall_data:
            overallsData.append(JobPostOverallExperience(job_post=instance, **overalls_data))
            
        bulk_sync(
            new_models = overallsData,
            filters = Q(job_post = instance),
            fields = remove_item_from_list(key='id', list =OverallExperienceSerializer.Meta.fields),
            key_fields = ['min_experience', 'max_experience']
            )

        benefitsData = []        
        for benefits_data in job_post_benefit_data:
            benefitsData.append(JobPostBenefits(job_post=instance, **benefits_data))
            
        bulk_sync(
            new_models = benefitsData,
            filters = Q(job_post = instance),
            fields = remove_item_from_list(key='id', list =BenefitsSerializer.Meta.fields),
            key_fields = ['name']
        )
        
        supplementPaysData = []
        for supplement_pays_data in job_post_supplement_pay_data:
            supplementPaysData.append(JobPostSupplementPay(job_post=instance, **supplement_pays_data))
            
        bulk_sync(
            new_models = supplementPaysData,
            filters = Q(job_post = instance),
            fields = remove_item_from_list(key='id', list =SupplementPaySerializer.Meta.fields),
            key_fields =['name']
            )

        return instance
    
    def destroy(self, instance):
        instance.delete()

    def validate_id(self, value):
        if not JobPost.objects.filter(creator=self.request.user, id=value).exits():
            raise serializers.ValidationError('Job not found')
        return value
 


class OnboardingBranchesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OnboardingBranches
        fields = ['onboarding_branches',]

class OnboardingSerializer(serializers.ModelSerializer):
    branches = OnboardingBranchesSerializer(many=True, required=False)
    
    class Meta:
        model = Onboarding
        fields = ['id', 'creator','onboarding_company_name', 'onboarding_industry', 'onboarding_scale', 'total_employees', 
                  'onboarding_company_vision', 'onboarding_company_values', 'onboarding_company_culture', 
                  'onboarding_linkedin', 'onboarding_website', 'onboarding_pan', 'onboarding_gst','onboarding_headquarter','onboarding_have_branches','branches',
                  ]
        
        extra_kwargs = {
            'creator': {'read_only': True},
        }
    
    
    def create(self, validated_data):
        
        branches_data = validated_data.pop('branches')
        
        onboarding = Onboarding.objects.create(**validated_data)
        
        branchData = []
        for branch_data in branches_data:
            branchData.append(OnboardingBranches(onboarding = onboarding, **branch_data))
        
        OnboardingBranches.objects.bulk_create(branchData)
            
        return onboarding
    
    
    def update(self, instance, validated_data):
        branches_data = validated_data.pop('branches')
        
        instance = super().update(instance, validated_data)
        
        branchData = []
        for branch_data in branches_data:
            branchData.append(OnboardingBranches(onboarding = instance, **branch_data))

        bulk_sync(
            new_models = branchData,
            filters=Q(onboarding = instance),
            fields=remove_item_from_list(key='id', list=OnboardingBranchesSerializer.Meta.fields),
            key_fields=['onboarding_branches']
        )   
        return instance
    
        
    def delete(self, instance):
        instance.delete()
          

########################################################################################################

    
