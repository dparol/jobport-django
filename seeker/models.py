from django.db import models
from main.models import Account,UserProfile
from recruiter.models import Jobapplication as Job

# Create your models here.
class uploadresume(models.Model):
    user = models.ForeignKey(Account,related_name='uploadresume',on_delete=models.CASCADE)
    resume = models.FileField()
    


    def __str__(self):
        return self.user.first_name


class candidateApplied(models.Model):
    job = models.ForeignKey(Job,related_name='related_jobname',on_delete=models.CASCADE)
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    candidate=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    applied_at=models.DateTimeField(auto_now_add=True)
    resume =models.ForeignKey(uploadresume,on_delete=models.CASCADE)

     

    def __str__(self):
        return self.job.job_title