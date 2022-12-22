from django.shortcuts import render
from .api.serializers import UserProfileserializer
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import api_view, APIView, permission_classes

from rest_framework import status
from rest_framework.status import HTTP_204_NO_CONTENT
from .models import UserProfile
from .api.serializers import UserProfileserializer

from .models import Account
from django.contrib import messages,auth
from django.shortcuts import redirect, render,get_object_or_404





from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage


from rest_framework.decorators import api_view

# Create your views here.
class register(CreateAPIView):
    serializer_class=UserProfileserializer
    def post(self,request):
        serializer= UserProfileserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()


            #email validation
            user=Account.objects.get(email=serializer.data['email'])

            current_site = get_current_site(request)
            mail_subject='Please activate your account'
            message = render_to_string('account_verification_email.html',{
                'user':user,
                'domain':current_site,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':default_token_generator.make_token(user),
                 
            })
            print(message)
            
            to_email=user.email
            send_email=EmailMessage(mail_subject,message,to=[to_email])
            send_email.send()



            return Response(serializer.data,status=status.HTTP_201_CREATED)

            




        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class activate(APIView):
    def post(self,request):
        uidb64=request.data['uidb64']
        token=request.data['token']


        try:
            uid=urlsafe_base64_decode(uidb64).decode()
            user =Account._default_manager.get(pk=uid)
        except(TypeError,ValueError,OverflowError,Account.DoesNotExist):
            user=None
        if user is not None and default_token_generator.check_token(user,token):
            user.is_active =True
            user.save()
            print(token)
            
            return Response(token,status=status.HTTP_200_OK)
        else:
            messages.error(request,'invalid activation link')
            return Response("verification faild",status=status.HTTP_400_BAD_REQUEST)
