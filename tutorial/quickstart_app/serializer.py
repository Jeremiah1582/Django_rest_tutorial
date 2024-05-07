from django.contrib.auth.models import Group, User #tables available by default
from rest_framework import serializers
from .models import Location 

#SERIALIZATION are used to turn the Python Objects in the DB into JSON that can be sent over the network

class UserSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta: 
        model = User #name of the table
        fields = ['url', 'username', 'email', 'groups'] #columns  of the table 
        
class GroupSerializers(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Group #name of the table 
        fields = ['url','name'] #columns  of the table 
        
        
class LocationSerializers(serializers.HyperlinkedModelSerializer): 
    
    country = serializers.CharField(label= 'country', max_length= 50)
    city = serializers.CharField(label= 'city', max_length= 50)
    road = serializers.CharField(max_length=50)
    number = serializers.IntegerField()
    postcode = serializers.CharField(max_length = 20)
    
    class Meta:
        model = Location 
        fields = [
            'url', # replaces PK in JSON. adds unique URL to the instance of this class
            'country',
            'city',
            'road',
            'number',
            'postcode'
            ]
        