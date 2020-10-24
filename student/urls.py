from django.contrib import admin
from django.urls import path, include
from django.views.generic import ListView, DetailView
from student.models import Student_TBL
from student.views import StudentLV,StudentDV
from student import views

app_name = 'student'
urlpatterns = [
    #Exmple:/student/
    path('',StudentLV.as_view(model=Student_TBL),name='index'),

    #Example:/student/index/
    path('<int:pk>/',StudentDV.as_view(model=Student_TBL),name='detail'),

    # Example: /studnet/search/
    path('search/', views.SearchFormView.as_view(), name='search'),
]
