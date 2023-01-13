from django.shortcuts import render
from .serializers import Jobserializer,QualificationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Jobapplication as Job,Qualification
from rest_framework.generics import CreateAPIView
from django.shortcuts import get_object_or_404
from rest_framework import status
from main.models import Account



from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import api_view, APIView, permission_classes

from main.models import RecruiterProfile

from rest_framework.pagination import PageNumberPagination

from django.db.models import Avg,Min,Max,Count

from .filters import jobfilter

# Create your views here.

@api_view(['GET'])

def getalljobs(request):
    filterset=jobfilter(request.GET,queryset=Job.objects.all().order_by('id'))
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

@api_view(['GET'])
def getjob(request,id):
    alljobs=get_object_or_404(Job,pk=id)
    serializer=Jobserializer(alljobs)
    return Response(serializer.data)



@permission_classes([IsAuthenticated])
class newjob(CreateAPIView):
    queryset = Job.objects.all()

    serializer_class=Jobserializer
    def post(self,request):
        current_user = request.user
        print(current_user)
        user=RecruiterProfile.objects.get(user=current_user)
        print(user)
        job_title=request.data['job_title']
        location=request.data['location']

        country=request.data['country']
        job_type=request.data['job_type']
        num_of_employees=request.data['num_of_employees']
        job_summery=request.data['job_summery']
        salary=request.data['salary']
        no_of_openings=request.data['no_of_openings']
        qualifications=request.data['qualifications']
        job_rule=request.data['job_rule']
        industry_type=request.data['industry_type']
        department=request.data['department']
        
        job=Job.objects.create(
            job_title=job_title,
            location=location,
            country=country,
            job_type=job_type,
            num_of_employees=num_of_employees,
            job_summery=job_summery,
            no_of_openings=no_of_openings,
            qualifications=qualifications,
            job_rule=job_rule,
            industry_type=industry_type,
            department=department,
            recruiter=user
        )
        
        
        serializer=Jobserializer(job,many=False)
        # job = Job.objects.get(recruiter__user=user)
        # job.recruiter = company
        # job.save()
        print(job)
        
        
        print(serializer.data)
        return Response(serializer.data)

class updatejob(CreateAPIView):
    serializer_class=Jobserializer
    def put(self,request,id):
        job=job.objects.get(pk=id)
        job.job_title=request.data['job_title']
        job.location=request.data['location']
        job.company_name=request.data['company_name']
        job.country=request.data['country']
        job.num_of_employees=request.data['num_of_employees']
        job.job_summery=request.data['job_summery']
        job.salary=request.data['salary']
        job.no_of_openings=request.data['no_of_openings']
        job.qualifications=request.data['qualifications']
        job.job_rule=request.data['job_rule']
        job.industry_type=request.data['industry_type']
        job.department=request.data['department']
        job.save()
        serializer=Jobserializer(job,many=False)
        return Response(serializer.data)
    

@api_view(['DELETE'])
def deletejob(request,id):
    job=Job.objects.get(pk=id)
    job.delete()
    return Response({'message':'job is Deleted'},status=status.HTTP_200_OK)




@api_view(['GET'])
def getTopicStats(request,topic):
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




