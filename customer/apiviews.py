from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response 
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer
from django.contrib.auth import authenticate

class LoginView(APIView):
    permission_classes = ()

    def post(self, request, ):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({ "token": user.auth_token.key })
        else:
            return Response({ "erroe": "Wrong Credentials" }, status=status.HTTP_400_BAD_REQUEST )

class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer
