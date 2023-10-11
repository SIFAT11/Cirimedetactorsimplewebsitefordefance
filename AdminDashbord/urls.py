from django.urls import path
from .views import *

urlpatterns = [
    path('adminpannel',index2,name='index2') ,
    path('accept_gd/<int:gd_id>/',accept_gd, name='accept_gd'),
    path('reject_gd/<int:gd_id>/',reject_gd, name='reject_gd'),  
    path('accept/',accept, name='accept'),
    path('reject/',reject, name='reject'),
    path('gd/<str:gd_id>/',gd_details, name='gd_details'),
    
    path('admin_pannel/admin_login/',admin_login, name='admin_login'),
    path('admin_logout/', admin_logout, name='admin_logout'),
    
    
    path('loginrequestjug/',loginrequest,name='loginrequestjug'),
    
    
    path('approve_judge/<int:judge_id>/',approve_judge, name='approve_judge'),
    path('reject_judge/<int:judge_id>/',reject_judge, name='reject_judge'),
    path('ad/judge/<int:judge_id>/',viewjudge_profile, name='judge_profile'),
    
    
    
    
    
    
    path('loginpo/',loginrequestpo, name='loginpo'),
    path('approve_police/<int:policeid>/',approve_Police, name='approve_police'),
    path('reject_police/<int:policeid>/',reject_police, name='reject_police'),
    path('viewpolice/<int:policeid>/',viewpolice_profile, name='viewpolice_profile')

]

