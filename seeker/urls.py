from django.urls import path
from . import views


urlpatterns = [
    path('showjobs',views.viewalljob,name='viewalljob'),
    path('uploadresume',views.AddResume.as_view(),name='AddResume'),
    # path('apply-job',views.ApplyJob.as_view(),name='ApplyJob'),
    path('searchtopic/<str:topic>/',views.Searchtopic.as_view(),name='Searchtopic')
]
