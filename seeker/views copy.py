from django.shortcuts import render
from .serializer import resumeserializer,CandidateSerializer
from rest_framework.decorators import api_view
from recruiter.models import Jobapplication as AllJobs
from recruiter.serializers import Jobserializer
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView,ListAPIView
from main.models import Account,UserProfile
from .models import uploadresume,candidateApplied

# Create your views here.
@api_view(['GET'])
def viewalljob(request):
    alljob=AllJobs.objects.all()
    serializer = Jobserializer(alljob)
    return Response(serializer.data)



class AddResume(CreateAPIView):
    serializer_class = resumeserializer
    def post(self,request):
        user_id = request.data['user']
        resume =request.data['resume']
        user = Account.objects.get(id=user_id)
        newresume=uploadresume.objects.create(
            user=user,
            resume=resume,
        )
        newresume.save()
        response={
            "message":"your resume uploaded successfully "
        }

        return Response(data=response)
    

class ApplyJob(CreateAPIView):
    serializer_class = CandidateSerializer
    def post(self,request):
        data=request.data
        job_id=data['job']
        user_id=data['user']
        try:
            alreadyapplied=candidateApplied.objects.get(job=job_id,user=user_id)
            
            response={
                "message":"you are already applied this job"
            }

            return Response(data=response)


        except:    
            
            user=Account.objects.get(pk=user_id)
            candidate=UserProfile.objects.get(user=user_id)

            job = AllJobs.objects.get(id=job_id)
            try:
                resume=uploadresume.objects.get(user=user)
                if resume :
                    newapplicant=candidateApplied.objects.create(
                        job=job,
                        user=user,
                        candidate=candidate,
                        resume=resume

                    )

            
            except Exception as e:
                print(e)
                response={
                "message":"you can't apply this job without resume...!"
                }
                return Response(data=response)
            response={
                "message":"Applied Successfully"
            }

            return Response(data=response)

            
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