from django.contrib import admin
from django.urls import path, include
from django.views.generic import ListView, DetailView
from namecard.models import Namecard_TBL
from namecard.views import NamecardLV,NamecardDV
from namecard import views

app_name = 'namecard'
urlpatterns = [
    #Exmple:/namecard/
    path('',NamecardLV.as_view(model=Namecard_TBL),name='index'),

    #Example:/namecard/index/
    path('<int:pk>/',NamecardDV.as_view(model=Namecard_TBL),name='detail'),

    # Example: /namecard/search/
    path('search/', views.SearchFormView.as_view(), name='search'),
]
