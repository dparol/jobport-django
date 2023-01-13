
from django.urls import path
from . import views




urlpatterns = [
    path('alljobs',views.getalljobs,name="getalljobs"),
    path('getjob/<int:id>',views.getjob,name='getjob'),
    path('newjob',views.newjob.as_view(),name='newjob'),
    path('updatejob/<int:id>/update',views.updatejob.as_view(),name='updatejob'),
    path('deletejob/<int:id>/delete',views.deletejob,name='deletejob'),
    path('getTopicStats/<str:topic>',views.getTopicStats,name='getTopicStats'),


 
 ]