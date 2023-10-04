# from user_app.models import Register
from django.contrib.auth.models import User 
# ! here we are using User Model which gives [username, email,password] by default
from rest_framework import serializers
from user_app.models import JobPost

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
    
    # min_length = 20
    # def validate_job_title(self, value):
    #     if value is None or len(value) == 0:
    #         raise serializers.ValidationError('This field is required')
        
    #     elif len(value) > self.min_length:
    #         message = 'The title length should be less than or equal to 20 characters'.format(self.min_length)
    #         raise serializers.ValidationError(message)
    #     return value
        
        

        