from rest_framework import generics

from . import models

from . import serialzers

#Used generics views 
class MenuView(generics.ListCreateAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serialzers.MenuSerializer
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)