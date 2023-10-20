from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, IsAdminUser  #? access 
from rest_framework import generics, permissions
from user_app.models import JobPost,Onboarding #? models
from . import serializers #? serializer
from django.contrib.auth.models import User
from config.custom_response import *
from django.core.exceptions import PermissionDenied #? permission


@api_view(['POST',])
def logout_view(request):

    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)



@api_view(['POST',])
def register_view(request):

    if request.method == 'POST':
        serializer = serializers.RegisterSerializer(data=request.data)

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

class PostListAPIView(generics.ListAPIView):
    
    permission_classes = [IsAuthenticated,]
    serializer_class = serializers.PostCreateSerializer
    
    def get_queryset(self):
        user = self.request.user
        return JobPost.objects.filter(creator=user)


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            message = 'you have not created any posts yet please create one'
            return sendError(message)
        else:
            serializer = self.get_serializer(queryset, many=True)
            return sendSuccess(serializer.data)
        
class PostCreateAPIView(generics.CreateAPIView):   
    
    permission_classes = [IsAuthenticated,]
    serializer_class  = serializers.PostCreateSerializer
    
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
        
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return sendSuccess(serializer.data)
        else:
            return sendError(serializer.errors)
    
    
class PostUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    
    permission_classes = [IsAuthenticated,]
    serializer_class = serializers.PostUpdateSerializer
    
    def get_queryset(self):
        user = self.request.user
        return JobPost.objects.filter(creator=user)
    
    def perform_update(self, serializer):
        job_post = self.get_object()
        if job_post.creator == self.request.user:
            serializer.is_valid(raise_exception=True)
            serializer.save()
        else:
            return validationError('you are not allowed to update this job post')
        
    def perform_destroy(self, instance):
        job_post = self.get_object()
        job_post_title = job_post.title
        if job_post.creator == self.request.user:
            job_post.delete()
            return sendSuccess(f'The Job {job_post_title} has been deleted successfully',)
        else:
            return validationError('You are not allowed to Delete the Job_post')
        

        
    
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated,])
def OnboardingListCreateView(request):    
    
    if request.method == 'GET':
        data = Onboarding.objects.filter(creator=request.user)
        if not data:
            return sendError('you dont have any items to display')
        
        serializer = serializers.OnboardingSerializer(data, many=True)
        return sendSuccess(serializer.data)
    
    elif request.method == 'POST':
        serializer = serializers.OnboardingSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(creator = request.user)
            return sendSuccess(serializer.data)
        else:
            message ='Please check and fill all the details correctly'
            return sendError(message)
        
# class CompanyList(generics.ListAPIView):
    
#     serializer_class = serializers.Onbo
    
        
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def OnboardingUpdateView(request, pk):
    
    
    if request.method == 'GET':
        
        user = Onboarding.objects.filter(creator=request.user, pk=pk)
        if not user:
            return sendError('you dont have any items to display and this is not your company to show the details..')
        
        serializer = serializers.OnboardingSerializer(user, many=True)
        return sendSuccess(serializer.data)
    
    if request.method == 'PUT':
    
        user = Onboarding.objects.filter(creator = request.user, pk=pk).first()
        if  not user:
            return sendError('you are not authorized to update this form as this is not created by you!! or you have not created any form to edit, please create one and try to edit')
        
        serializer = serializers.OnboardingSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(creator = request.user)
        return sendSuccess(serializer.data)
        
    
         
    elif request.method == 'DELETE':
        
        data = Onboarding.objects.filter(creator = request.user, pk=pk)
        if not data:
            return sendError('you are not authorized to delete this form as this is not created by you!! or you have no form to update, please create one and delete')
        
        data.delete()
        return sendSuccess(f'data deleted success')
                
#################################################################  

# class OnboardingListView(generics.ListCreateAPIView):
#     queryset = Onboard.objects.all()
#     serializer_class = serializers.OnboardingBranchSerializer
        
        
        
# class OnboardingView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Onboard.objects.all()
#     serializer_class = serializers.OnboardingBranchSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def perform_update(self, serializer):
#         # Only allow the creator to update the onboarding
#         if serializer.instance.creator == self.request.user:
#             serializer.save()
#         else:
#             raise PermissionDenied("You are not allowed to update this onboarding.")

#     def perform_destroy(self, instance):
#         # Only allow the creator to delete the onboarding
#         if instance.creator == self.request.user:
#             instance.delete()
#         else:
#             raise PermissionDenied("You are not allowed to delete this onboarding.")
        
            
