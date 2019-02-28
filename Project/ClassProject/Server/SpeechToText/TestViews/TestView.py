from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.views import APIView
from SpeechToText.serializers import UserSerializer
from SpeechToText.models import User
# Create your views here.

class TestAPIView(APIView):
    
    def get(self, request):
        print(id)
        return Response("Test Get")

    

    def post(self, request, format = None):
        print(request.data)
        #serializer = UserSerializer(data = request.data)
        return Response("Test Post", HTTP_200_OK)
