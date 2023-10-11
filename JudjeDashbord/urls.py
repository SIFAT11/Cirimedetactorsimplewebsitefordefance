from django.urls import path
from .views import *

urlpatterns = [
      path('home3/',index3, name='index3'),
      path('jugregister/',jugregister, name='jugregister'),
      path('juglogin/',juglogin, name='juglogin'),
      path('jug_logout/',jug_logout, name='jug_logout'),
      path('jugreset/',jugreset, name='jugreset'),
      path('acceptgd/',acceptgd, name='acceptgd'),
      path('gdview/<str:gd_id>/',gdview,name='gdview'),
]
