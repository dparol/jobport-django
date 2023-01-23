from django.shortcuts import render
from .api.serializers import UserProfileserializer
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import api_view, APIView, permission_classes

from django.contrib.auth.hashers import make_password

from rest_framework import status
from rest_framework.status import HTTP_204_NO_CONTENT
from .models import UserProfile
from .api.serializers import UserProfileserializer,RecruiterProfileSerializer,RecruiterdetailsSerializer
from django.views.decorators.csrf import csrf_exempt

from .models import Account
from django.contrib import messages,auth
from django.shortcuts import redirect, render,get_object_or_404


from .models import RecruiterProfile

from rest_framework.permissions import IsAuthenticated, IsAdminUser


from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage


from rest_framework.decorators import api_view


from recruiter.models import Jobapplication
from recruiter.serializers import Jobserializer
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
    
    def post(self,request,uid,token):
        uidb64=uid
        token=token
        print(uidb64)
        print(token)

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


        

class company_reg(CreateAPIView):
    print("hi register")
    serializer_class=RecruiterProfileSerializer
    def post(self,request):
        data=request.data

        try:
            user =request.user
            new_company=RecruiterProfile.objects.create(user=user,**data)
            serializer=RecruiterProfileSerializer(new_company,many=False)

            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
         
            return Response("verification faild",status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAdminUser])

def AllCompanyProfile(request):
    allcompany=RecruiterProfile.objects.filter(is_pending=True)
    
    serializer=RecruiterProfileSerializer(allcompany,many=True)
    
    return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAdminUser])

def Accept_Company(request):
    data=request.data
    email=request.data['email']
   
    allcompany=RecruiterProfile.objects.get(company_mail=email)
    allcompany.is_approved=True
    allcompany.is_pending=False
    allcompany.save()
    serializer=RecruiterProfileSerializer(allcompany)
    print(serializer.data)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])

def Reject_Company(request):
    data=request.data
    email=request.data['email']
    print(email)
    allcompany=RecruiterProfile.objects.get(company_mail=email)
    allcompany.is_approved=False
    allcompany.is_pending=False
    allcompany.is_rejected=True
    allcompany.save()
    serializer=RecruiterProfileSerializer(allcompany)
    return Response(serializer.data)



@api_view(['GET'])
@permission_classes([IsAdminUser])

def AcceptedCompanies(request):
    allcompany=RecruiterProfile.objects.filter(is_approved=True)
    
    serializer=RecruiterProfileSerializer(allcompany,many=True)
    print(serializer.data)
    return Response(serializer.data)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def currentuser(request):
    user=UserProfileserializer(request.user)
    return Response(user.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllrecruiters(request):
    allrecruiters=Account.objects.filter(is_recruiter=True)
    serializer =RecruiterdetailsSerializer(allrecruiters,many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getallCandidate(request):
    allcandidates =Account.objects.filter(is_recruiter=False)
    serializer = RecruiterdetailsSerializer(allcandidates,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def totalJobs(request):
    allJobs = Jobapplication.objects.all()
    serializer =Jobserializer(allJobs,many=True)
    return Response(serializer.data)
    


# @api_view(['PUT'])
# @permission_classes([IsAuthenticated])
# def updateUser(request):
#     user=request.user
#     print(user.first_name)
#     data=request.data
#     user.first_name=data['first_name']
#     user.last_name=data['last_name']
#     user.username=data['username']
#     user.email=data['email']
#     user.phone_number=data['phone_number']
#     if data['password'] != '':
#         user.password =make_password(data['password'])

#     user.save()
#     serializer=UserProfileserializer(user)
#     return Response(serializer.data)