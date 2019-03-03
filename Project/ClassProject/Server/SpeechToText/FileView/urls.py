from .FileView import UploadedFileView
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path
from django.conf.urls import url


urlpatterns = [
    #url(r'^login/', UserListAPIView.as_view(), name = 'Login'),
    url(r'^files/$', UploadedFileView.as_view(), name = 'Files-View'),
    url(r'^files/(?P<id>\d+)/$', UploadedFileView.as_view(), name = 'Files-View'),


]