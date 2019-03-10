import pytest
import unittest
from django.contrib.auth.models import User
from SpeechToText.models import File, FileType
from django.core.files import File as djFile
from django.core.files.base import ContentFile
import os
import requests
#from rest_framework.authtoken.models import Token
from knox.models import AuthToken

import json
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test.client import BOUNDARY, MULTIPART_CONTENT, encode_multipart, Client, RequestFactory
from rest_framework.test import APIClient

@pytest.fixture(autouse=True)
def cleanup_files():
    pass
    #files = []
        # monkeypatch.setattr(builtins, 'open', patch_open(builtins.open, files))
        # monkeypatch.setattr(io, 'open', patch_open(io.open, files))
        # yield
        # for file in files:
        #     os.remove(file)

@pytest.mark.django_db
class TestFiles:

    def setup(self):
        user_obj = User.objects.create_user(username = "cesar", password="1234", email="cls33@njit.edu")
        user_obj.save()

        audio_type = FileType.objects.create(id = 1, Name='Audio')
        audio_type.save()
        video_type = FileType.objects.create(id = 2, Name='Video')
        video_type.save()

        audio_path = os.getcwd() + '/Test/TestFiles/AudioTestFile1.mp3'
        f = open(audio_path, 'rb')
        audiotest1 = djFile(f)
        file_obj_Audio = File.objects.create(Name='Audio File', Type = audio_type, User = user_obj)
        file_obj_Audio.Content = audiotest1
        file_obj_Audio.save()


    def teardown_method(self, method):
        file_obj_Audios = File.objects.all()

        #Cleaingin files
        for f in file_obj_Audios:
            f.delete()

    def test_PostAudioFileMp3(self, client):
        #get Token
        token = AuthToken.objects.create(User.objects.first())
        #Get Audio file mp3
        audio_path = os.getcwd() + '/Test/TestFiles/AudioTestFile1.mp3'
        f = open(audio_path, 'rb')
        audio = SimpleUploadedFile(audio_path, content = f.read(), content_type="audio/mp3")
        #Preparing data
        data = { 'Type' : 1, 'Name' : 'Tes1', 'Content' : audio}
        
        #Authenticating user
        cl = APIClient()
        cl.credentials(HTTP_AUTHORIZATION='Token ' + token)
        #Calling endPoint
        response = cl.post('/account-files/files/', data=data)
        assert response.status_code == 201


    def test_GetAudioFileList(self, client):
        #get Token
        token = AuthToken.objects.create(User.objects.first())
        
        #Authenticating user
        cl = APIClient()
        cl.credentials(HTTP_AUTHORIZATION='Token ' + token)
        #Calling EndPoint
        response = cl.get('/account-files/files/')
        
        assert len(response.data) == File.objects.count()


    def test_GetAudioFileByID(self, client):
        #get Token
        token = AuthToken.objects.create(User.objects.first())
        
        id  = File.objects.first().id
        #Authenticating user
        cl = APIClient()
        cl.credentials(HTTP_AUTHORIZATION='Token ' + token)
        #Calling EndPoint
        response = cl.get('/account-files/files/' + str(id) + "/")
        assert response.data[0]['id'] == id

    def test_DeleteAudioFileByID(self, client):
        #get Token
        token = AuthToken.objects.create(User.objects.first())
        
        id  = File.objects.first().id
        #Authenticating user
        cl = APIClient()
        cl.credentials(HTTP_AUTHORIZATION='Token ' + token)
        #Calling EndPoint
        response = cl.delete('/account-files/files-delete/' + str(id) + "/")
        assert response.status_code == 204
