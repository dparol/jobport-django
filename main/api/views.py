from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view,permission_classes
from rest_framework import generics
from .serializers import UserProfileserializer
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