from django.urls import path
from .views import *

urlpatterns = [
    path('polic-login/',polic_login, name='policlogin'),
    path('polic-logout/',polic_logout, name='policlogout'),
    path('polic-reset/',polic_reset, name='polic_reset'),
    path('polic-register/',polic_register, name='polic_register'),
    path('po/',poacceptgd,name='poacceptgd'),
    path('index4/',index4,name='index4'),
    path('gdpoview/<str:gd_id>/',gdpoview,name='gdpoview'),
]
