from django.db import models
from main.models import RecruiterProfile

from django.core.validators import MinValueValidator,MaxValueValidator



# Create your models here.
skills=[
    ("py","python"),
    ("jv","java"),
    ("js","java_script"),
    ("php","PHP"),
    ("rb","RUBY"),
    ("C","C"),


]


jobtype=[
    ("permanent","permanent"),
    ("Temporary","Temporary"),
    ("intership","intership"),
]

education=[
    ("bachlors","bachlors"),
    ("masters","masters"),
    ("phd","phd"),
    
]
industry=[
    ("Business","Business"),
    ("it","IT/SOFTWARE"),
    ("banking","Banking"),
    ("education","Education"),
    ("telecommunication","telecommunication"),
    ("others","Others")

]

experiace=[
    ("fresher","Fresher"),
    ("one_yesr","1 year"),
    ("two_year","2 year"),
    ("fresher","Fresher"),
    ("fivce_year","5 year"),
]

class Jobapplication(models.Model):
    job_title=models.CharField(max_length=500)
    location =models.CharField(max_length=100)
    recruiter=models.ForeignKey(RecruiterProfile,on_delete=models.CASCADE,null=True,blank=True)
    country =models.CharField(max_length=500)
    job_type=models.CharField(max_length=500,choices=jobtype)
    num_of_employees=models.CharField(max_length=500)
    job_summery=models.CharField(max_length=500)
    responsibility=models.CharField(max_length=500)
    qualifications=models.CharField(max_length=500)
    salary=models.IntegerField(default=1,validators=[MinValueValidator(1),MaxValueValidator(10000)],null=True,blank=True)
    
    no_of_openings=models.IntegerField()
    job_rule=models.CharField(max_length=500)
    industry_type=models.CharField(max_length=200,
                choices=industry
    )
    department=models.CharField(max_length=200)
    date_created  =models.DateTimeField(auto_now_add=True,null=True,blank=True)
    experiance=models.CharField(max_length=500,choices=experiace,null=True,blank=True)
    education=models.CharField(max_length=500,choices=education,null=True,blank=True)
    skill=models.CharField( max_length = 20,
        choices = skills,null=True,blank=True
        )
    def __str__(self):
        return self.job_title
    

class Qualification(models.Model):
    Jobapplication = models.ForeignKey(Jobapplication, related_name='Qualification', on_delete=models.CASCADE)
    year_of_exp=models.IntegerField()
    education=models.CharField(max_length=500,choices=education)
    skill=models.CharField( max_length = 20,
        choices = skills
        )
    


