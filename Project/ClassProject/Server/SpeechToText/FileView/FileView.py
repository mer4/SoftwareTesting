from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework import generics, mixins
from rest_framework.response import Response
from SpeechToText.permissions import IsOwner, PublicEndpoint
from .serializers import FileSerializer
from SpeechToText.models import File

class UploadedFileView(mixins.CreateModelMixin,generics.ListAPIView):
    lookup_field            = 'id'
    serializer_class        = FileSerializer
    permission_classes      = [IsOwner]

    def get_queryset(self, *args, **kwargs):
        qs = File.objects.filter(User = self.request.user)
        print('Checking')
         
        if "id" in self.kwargs:
            qs = qs.filter(id = int(self.kwargs["id"])).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(User=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class DeleteFileView(generics.DestroyAPIView):
    lookup_field            = 'id' 
    serializer_class = FileSerializer
    permission_classes = [IsOwner]
    queryset = File.objects.all()
    
        
   