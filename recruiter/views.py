from django.shortcuts import render
from .serializers import Jobserializer,QualificationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Jobapplication as Job,Qualification
from rest_framework.generics import CreateAPIView
from django.shortcuts import get_object_or_404
from rest_framework import status
from main.models import Account
from main.models import UserProfile
from main.api.serializers import UserProfileserializer,CandidateprofileSerializer
from django.db.models import Avg,Min,Max,Count
from seeker.models import candidateApplied



from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import api_view, APIView, permission_classes

from main.models import RecruiterProfile
from seeker.serializers import CandidateSerializer



# Create your views here.





@permission_classes([IsAuthenticated])
class newjob_list(CreateAPIView):


    queryset = Job.objects.all()

    serializer_class=Jobserializer
    def post(self,request):
        current_user = request.user

        user=RecruiterProfile.objects.get(user=current_user)
        data =request.data
        
        job =Job.objects.create(recruiter=user,**data)
        serializer =Jobserializer(job,many=False)
        return Response(serializer.data)
    
    def get(self,request):
        job = Job.objects.all()
        serializer =Jobserializer(job,many=True)
        return Response(serializer.data)


        
@permission_classes([IsAuthenticated])

class singlejob_details(CreateAPIView):
    serializer_class=Jobserializer
    def put(self,request,id):
        job=Job.objects.get(pk=id)
        serializer = Jobserializer(job, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def get(self,request,id):
        try:
            alljobs=Job.objects.get(pk=id)
            serializer=Jobserializer(alljobs,many=False)
            return Response(serializer.data)
        except:
            return Response({'message':"The job is not available"}, status=status.HTTP_400_BAD_REQUEST)
       
    def delete(self,request,id):
        try:
            job=Job.objects.get(pk=id)
            if job.recruiter != request.user:
                return Response({"message":"you can't delelte this job" },status=status.HTTP_403_FORBIDDEN)
            job.delete()
            return Response({'message':'job is Deleted'},status=status.HTTP_200_OK)
        except:
            return Response({'message':"sorry,the specified job we can't get"}, status=status.HTTP_400_BAD_REQUEST)




@permission_classes([IsAuthenticated])

@api_view(['GET'])
def getTopicStatus(request,topic):
    args={'job_title__icontains':topic}
    jobs=Job.objects.filter(**args)
    if len(jobs)==0:
        return Response({'message':'Not Found for {topic}'.format(topic=topic)})

    stats=jobs.aggregate(
        total_jobs=Count('job_title'),
        avg_positions=Avg('salary'),
        min_salary=Min('salary'),
        max_salary=Max('salary')
    )
         
    return Response(stats)


@permission_classes([IsAuthenticated])

@api_view(["GET"])
def allcandidates(request):
    allapplicants = UserProfile.objects.all()
    serializer = CandidateprofileSerializer(allapplicants, many = True)
    return Response(serializer.data)



@permission_classes([IsAuthenticated])

@api_view(['GET'])
def appliedcandidate(request,id):
    user =request.user
    print(user)
    try:
        job = Job.objects.get(recruiter__user = user, pk = id)
        jobposted = candidateApplied.objects.filter(job=job)
        print(jobposted)
        serializer = CandidateSerializer(jobposted,many=True)
        return Response(serializer.data)
    except Exception as e:
        print(e)
        return Response("error")


    
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def searchCandidate(request,topic):
    args ={
        "description__icontains":topic,
    }
    filterdCandidates = UserProfile.objects.filter(**args)
    if len(filterdCandidates)==0:
        return Response({'message':'Not Found for {topic}'.format(topic=topic)})
    serializer =CandidateprofileSerializer(filterdCandidates,many=True)
    
    return Response(serializer.data)


