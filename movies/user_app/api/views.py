from rest_framework.decorators import api_view
from user_app.api.serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from user_app import models



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

            # ! here we are getting the token and adding it to user_data api!! 
            # token = Token.objects.get(user = user).key
            # user_data['result']['token'] = token

            for user in User.objects.all():
                token = Token.objects.get_or_create(user=user).key
            user_data['result']['token'] = token

        
        else:
            user_data['message'] = 'UnSuccessful'  # ! if the  data is not valid , then this will override the [message and status] fields.
            user_data['status'] = 'Fail'
            return Response(user_data, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(user_data)
        