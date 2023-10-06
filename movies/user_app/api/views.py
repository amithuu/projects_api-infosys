from rest_framework.decorators import api_view
from user_app.api.serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics, permissions
from user_app.models import JobPost, Job_Post
from . import serializers
from django.contrib.auth.models import User
from config.custom_response import *
from django.core.exceptions import PermissionDenied


@api_view(['POST',])
def logout_view(request):

    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)



@api_view(['POST',])
def register_view(request):

    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)

        # ? creating the dictionary to send the data in json format to api!! 
        user_data ={'message' : "Successfully sending the user",
                    'status' : "success",

            "result":{

        },
                    }
        
        if serializer.is_valid():
            user = serializer.save() 
            # * when we call the save() method which we have overridden we get some return 'user', 
            # * we are storing it in 'user' variable to access the objects..! and send api response

            user_data['result']['username'] = user.username
            user_data['result']['email'] = user.email

            # ! here we are getting the token and adding it to user_data api!! we are using Token.Models for this
            # token = Token.objects.get(user = user).key
            # user_data['result']['token'] = token

            # for user in User.objects.all():
            #     token = Token.objects.get_or_create(user=user).key
            # user_data['result']['token'] = token

            refresh = RefreshToken.for_user(user)
            user_data['result']['token'] = {
                'refresh': str(refresh),
                'access' :str(refresh.access_token),
            }
        
        else:
            user_data['message'] = 'UnSuccessful'  # ! if the data is not valid , then this will override the [message and status] fields.
            user_data['status'] = 'Fail'
            return Response(user_data, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(user_data)

class JobPostListCreate(generics.ListCreateAPIView):
    
    permission_classes = [IsAuthenticated,IsAdminUser]
    serializer_class = serializers.JobPostSerializer
    
    def get_queryset(self):
        user = self.request.user
        queryset = JobPost.objects.filter(created_by = user)
        if queryset.exists():
            return queryset
        else:
            return validationError('you have not added any Jb_pOst please add to View')
            

    
    def perform_create(self, serializer):
        
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save(created_by = self.request.user)
            data = serializer.data
            return sendSuccess(data)
            
        except Exception as e:
            user_data = {
                "error": str(e)
            }
            return sendError(user_data)
    
    
class JobPostUpdate(generics.RetrieveUpdateDestroyAPIView):
    
    permission_classes = [IsAuthenticated,IsAdminUser]
    queryset = JobPost.objects.all()
    serializer_class = serializers.JobPostSerializer

    def perform_update(self, serializer):
        job_post = self.get_object()
        if job_post.created_by == self.request.user:
            serializer.save()
        else:
            raise PermissionDenied("You are not allowed to update this job post.")

    def perform_destroy(self, instance):
        if instance.created_by == self.request.user:
            instance.delete()
        else:
            raise PermissionDenied("You are not allowed to delete this job post.")



class Job_PostList(generics.ListAPIView):
    
    permission_classes = [IsAuthenticated,]
    serializer_class = serializers.Job_PostSerializer

    def get_queryset(self):
        user = self.request.user
        return Job_Post.objects.filter(creator=user)


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            message = 'you have not created any posts yet please create one'
            return sendError(message)
        else:
            serializer = self.get_serializer(queryset, many=True)
            return sendSuccess(serializer.data)
        
class Job_PostCreate(generics.CreateAPIView):
    
    permission_classes = [IsAuthenticated,]
    serializer_class  = serializers.Job_PostSerializer
    
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
        
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(creator=self.request.user)
            return sendSuccess(serializer.data)
        else:
            return sendError(serializer.errors)
    
    
class Job_PostDetail(generics.RetrieveUpdateDestroyAPIView):
    
    permission_classes = [IsAuthenticated,]
    serializer_class = serializers.Job_PostSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Job_Post.objects.filter(creator=user)
    
    def perform_update(self, serializer):
        job_post = self.get_object()
        if job_post.creator == self.request.user:
            serializer.is_valid(raise_exception=True)
            serializer.save()
        else:
            return validationError('you are not allowed to update this job post')
        
    def perform_destroy(self, serializer):
        job_post = self.get_object()
        if job_post.creator == self.request.user:
            job_post.delete()
        else:
            return validationError('You are not allowed to Delete the Job_post')
        

        
    
    
    
    

        
            
        

