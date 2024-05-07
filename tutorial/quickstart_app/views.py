from rest_framework import permissions, viewsets
from quickstart_app.serializer import GroupSerializers, UserSerializer, LocationSerializers
from django.contrib.auth.models import User, Group
from .models import Location

# class based Views.

class UserViewSet(viewsets.ModelViewSet): 
    
    """ Each class viewset is an API endpoint accessible by users. 
        allowing users to view or edit Users"""
    
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes =[permissions.IsAuthenticated]
    
    
    
class GroupViewSet(viewsets.ModelViewSet): 

    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializers
    permission_classes =[permissions.IsAuthenticated]
    
    
class LocationViewSet(viewsets.ModelViewSet): 
    queryset = Location.objects.all().order_by('city')
    serializer_class = LocationSerializers
    
    
    