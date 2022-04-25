from django.urls import path
from myguest import views


urlpatterns = [
   path('', views.ListFunc),
   path('insert', views.insert),
   path('insertOk', views.insertOk),
]
