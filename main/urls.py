
from django.urls import path
from . import views




urlpatterns = [
    path('register',views.register.as_view(),name="create_account"),
    path('activate/',views.activate.as_view(),name='activate'),


 ]