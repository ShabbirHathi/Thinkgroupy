from django.urls import path
from .views import *


urlpatterns = [


    path('api/create/',createview,name='create'),
    path('api/read/',readview,name='read'),
    path('api/update/<int:pk>/',updateview,name='update'),
    path('api/delete/<int:pk>/',deleteview,name='delete'),


   
]