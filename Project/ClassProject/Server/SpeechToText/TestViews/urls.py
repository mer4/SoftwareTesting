from .TestView import TestAPIView
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path
from django.conf.urls import url


urlpatterns = [
    #url(r'^login/', UserListAPIView.as_view(), name = 'Login'),
    url(r'^$', TestAPIView.as_view(), name = 'Test-View')

]