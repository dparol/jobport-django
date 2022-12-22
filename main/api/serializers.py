from rest_framework import serializers
from ..models import UserProfile,Account
 
 
class UserProfileserializer(serializers.ModelSerializer):
    class Meta:
       model = Account
       fields =['username','email','phone_number','password']

    def create(self,validated_data):
        password=validated_data.pop('password')
        user=super().create(validated_data)
        user.set_password(password)
        user.save()
        return user