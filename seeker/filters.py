from django_filters import rest_framework as filters
from recruiter.models import Jobapplication as Job


class jobfilter(filters.FilterSet):
    keyword=filters.CharFilter(field_name="job_title",lookup_expr="icontains")
    location=filters.CharFilter(field_name="location",lookup_expr="icontains")
    min_salary = filters.NumberFilter(field_name="salary" or 0,lookup_expr='gte')
    max_salary = filters.NumberFilter(field_name="salary" or 10000,lookup_expr='lte')
    class Meta:
        model =Job
        fields = ('keyword','education','job_type','experiance')