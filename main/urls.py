
from django.urls import path
from . import views




urlpatterns = [
    path('register',views.register.as_view(),name="create_account"),
    path('activate/<str:uid>/<str:token>/',views.activate.as_view(),name='activate'),
    path('company_register',views.company_reg.as_view(),name='company_register'),
    path('company/details/',views.AllCompanyProfile,name='AllCompanyProfile'),
    path('company/accept/',views.Accept_Company,name='Accepted_Company'),
    path('company/reject/',views.Reject_Company,name='Reject_Company'),
    path('company/approved/',views.AcceptedCompanies,name='approved'),
    path('currentuser/',views.currentuser,name="currentuser"),
    path('get/allrecruiters/',views.getAllrecruiters,name="getAllrecruiters"),
    path('get/allcandidate/',views.getallCandidate,name='getallCandidate'),
    path('get/totaljobs/',views.totalJobs,name='totalJobs')
    

 ]