from rest_framework.decorators import api_view
from user_app.api.serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST',])
def register_view(request):

    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        