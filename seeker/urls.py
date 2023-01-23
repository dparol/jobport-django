from django.urls import path
from . import views


urlpatterns = [
    path('showjobs',views.viewalljob,name='viewalljob'),
    path('uploadresume',views.AddResume.as_view(),name='AddResume'),
    path('apply_job/<int:id>/',views.ApplyJob.as_view(),name='ApplyJob'),
    path('searchtopic/<str:topic>/',views.Searchtopic.as_view(),name='Searchtopic'),
    path('alljobs',views.getalljobs,name="getalljobs"),
    path('appliedjobs',views.appliedjobs,name='appliedjobs'),
    # path('editprofile/<int:id>',views.editProfile.as_view(),name='editProfile')
]
