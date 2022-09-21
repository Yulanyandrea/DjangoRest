from rest_framework import serializers
from api.models import User


class UserSerializer(serializers.ModelSerializer):
    

    class Meta:
        model=User
        fields=['id','username','password','name','email']
    
    def create(self, validated_data): #recibe un JSON y lo convierte a objeto
        
        userInstance=User.objects.create(**validated_data)
        return userInstance

    def to_representation(self, obj): #recibe un objeto y lo convierte a JSON 
        user=User.objects.get(id=obj.id)
        
        return{
            'id':user.id,
            'username':user.username,
            'name':user.name,
            'email':user.email,
            
        }