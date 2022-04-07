# main urls.py로 부터 위임받은 urls
from django.urls import path
from gtApp import views

urlpatterns = [ 
    path('insert', views.insertFunc),
    # path('inserted', views.insertedFunc),
    
]