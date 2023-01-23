
from django.urls import path
from . import views


urlpatterns = [
    
    path('newjob_list',views.newjob_list.as_view(),name='newjob_list'),
    path('singlejob_details/<int:id>/',views.singlejob_details.as_view(),name='singlejob_details'),
    path('getTopicStatus/<str:topic>',views.getTopicStatus,name='getTopicStatus'),
    path('allcandidates',views.allcandidates,name='allcandidates'),
    path('appliedcandidate/<int:id>',views.appliedcandidate,name='appliedcandidate'),
    path('searchCandidate/<str:topic>',views.searchCandidate,name='searchCandidate')
]