from rest_framework import serializers
from ..models import UserProfile,Account,RecruiterProfile

 
 
class UserProfileserializer(serializers.ModelSerializer):

    class Meta:
       model = Account
       fields =['username','email','phone_number','password','is_recruiter']

    def create(self,validated_data):
        password=validated_data.pop('password')
        user=super().create(validated_data)
        user.set_password(password)
        user.save()
        return user

class RecruiterProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model= RecruiterProfile
        fields=['user','company_name','designation','location','company_GST','company_mail','is_approved','is_pending','is_rejected']
        
    
class CandidateprofileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields ='__all__'       

class RecruiterdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model =Account
        fields = ['username','email','phone_number']