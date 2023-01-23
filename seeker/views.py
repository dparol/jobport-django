from django.shortcuts import render
from .serializers import resumeserializer,CandidateSerializer
from rest_framework.decorators import api_view
from recruiter.models import Jobapplication as AllJobs
from recruiter.serializers import Jobserializer
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView,ListAPIView
from main.models import Account,UserProfile
from .models import uploadresume,candidateApplied
from main.models import   RecruiterProfile
from main.api.serializers import UserProfileserializer,RecruiterdetailsSerializer
from rest_framework import status



from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import api_view, APIView, permission_classes


from rest_framework.pagination import PageNumberPagination


from .filters import jobfilter

# Create your views here.
@api_view(['GET'])
def viewalljob(request):
    alljob=AllJobs.objects.all()
    serializer = Jobserializer(alljob,many=True)
    return Response(serializer.data)



@permission_classes([IsAuthenticated])

class AddResume(CreateAPIView):
    serializer_class = resumeserializer
    def post(self,request):
        data=request.data
        user=request.user
        resume=data['resume']
        newresume=uploadresume.objects.create(
            user=user,
            resume=resume,
        )
        newresume.save()
        response={
            "message":"your resume uploaded successfully "
        }

        return Response(data=response)
    
@permission_classes([IsAuthenticated])

class ApplyJob(CreateAPIView):
    serializer_class = CandidateSerializer
    def post(self,request,id):
        user=request.user
        job =AllJobs.objects.get(pk=id)
        candidate=UserProfile.objects.get(user=user)
        resume=uploadresume.objects.get(user=user)
       
        already_applyed = candidateApplied.objects.filter(user=user,job=job)
        if already_applyed:
            response={
                 "message":"you are already applied this job"
             }

            return Response(data=response)
        else:
            new_applicant = candidateApplied.objects.create(
                user=user,
                job=job,
                candidate= candidate,
                resume=resume

            )
            new_applicant.save()
            response={
                 "message":"Applied Successfully"
             }

            return Response(data=response)


        
@permission_classes([IsAuthenticated])
            
class Searchtopic(ListAPIView):
    serializer_class = Jobserializer
    queryset = AllJobs.objects.all()
    def get(self,request,topic):
        
        q = {"job_title__icontains":topic}
        result = AllJobs.objects.filter(**q)
        if len(result)==0:
            return Response({"message":"Not Result"})
        serializer = Jobserializer(result,many=True)
        return Response(serializer.data)


@api_view(['GET'])

def getalljobs(request):
    filterset=jobfilter(request.GET,queryset=AllJobs.objects.all().order_by('id'))
    # alljobs = Job.objects.all()
    # pagination

    count = filterset.qs.count()
    resPerPage =3
    
    paginator=PageNumberPagination()
    paginator.page_size =resPerPage

    queryset = paginator.paginate_queryset(filterset.qs,request)



    serializer=Jobserializer(queryset,many=True)
    return Response({
        "count":count,
        "resPerPage":resPerPage,
        "jobs":serializer.data,
        
         })


@permission_classes([IsAuthenticated])

@api_view(['GET'])
def appliedjobs(request):
    args = {'user':request.user}
    jobs = candidateApplied.objects.filter(**args)
    serializer =CandidateSerializer(jobs,many=True)

    print(jobs)
    return Response(serializer.data)



# class editProfile(CreateAPIView):
#     serializer_class = UserProfileserializer
#     def put(self,request,id):
#         user=request.user

#         profile=Account.objects.get(user=user,pk=id)
#         serializer = RecruiterdetailsSerializer(profile,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        






