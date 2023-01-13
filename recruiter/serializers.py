from rest_framework import serializers
from recruiter.models import Jobapplication,Qualification

class Jobserializer(serializers.ModelSerializer):
    class Meta:
        model = Jobapplication
        fields =("job_title","location","country","num_of_employees","job_summery","responsibility","qualifications","salary","no_of_openings","job_rule","industry_type","department","date_created","experiance","education","skill")

class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields ="__all__"
        
    