from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view,permission_classes
from rest_framework import generics
from .serializers import UserProfileserializer,RecruiterProfileSerializer
from rest_framework.response import Response
from main.models import Account







#api tokens
class RegisterView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = UserProfileserializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email

        token['is_superadmin']=user.is_superadmin
        token['is_staff']=user.is_staff

        
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer




@api_view(['GET'])
def getRoutes(request):
    routes=[
        '/api/token',
        '/api/token/refresh'
    ]
    
    return Response(routes)



# @api_view(['GET'])
# def adminuser(request,id):

#     user=request.get(pk=id)
#     admin=user.objects.get(is_superadmin=True)
#     try:





