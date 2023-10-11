from django.urls import path
from .views import *

urlpatterns = [
    path('gd/',GD,name='GD'),
    path('do/',home,name='home'),
    path('login/',login,name='login'),
    path('register/',Register,name='register'),
    path('',loginoption,name='loginoption'),
    path('log_out/',log_out, name='logout'),
    path('reset/',reset, name='reset'),
     path('gd/list/',TotalGD, name='TotalGD'),
]
