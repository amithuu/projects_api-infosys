from rest_framework.decorators import api_view
from user_app.api.serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics 
from user_app.models import JobPost
from . import serializers
from django.contrib.auth.models import User


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
    
    # permission_classes = [IsAuthenticated,]
    serializer_class = serializers.JobPostSerializer
    queryset = JobPost.objects.all()

    
    def perform_create(self, serializer):
        
        try:
            serializer.save()
            data = serializer.data
            user_data ={'message' : "Successfully sending the user",
                        'status' : "success",
                        "result":{ data }
            }
            print(data)
            return Response(user_data, status=status.HTTP_201_CREATED,  content_type='application/json')
        
        except Exception as e:
            response_data = {
                "message": "Error creating JobPost",
                "status": "error",
                "error": str(e)
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST,  content_type='application/json')
    
    
class JobPostUpdate(generics.RetrieveUpdateDestroyAPIView):
    
    # permission_classes = [IsAuthenticated,]
    queryset = JobPost.objects.all()
    serializer_class = serializers.JobPostSerializer

    