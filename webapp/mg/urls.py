from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView # <--
from . import views
urlpatterns = [
    path('log',views.InfoView),  
    path('doctor',view=views.DoctorView),
    path('doctors',view=views.DetailView),
    path('patient',views.PatientView) ,
    path('recommendation',views.RecommendView) ,
    path('',views.Index),
    path('forum',views.Forum),
    path('createQuestion',views.CreateQuestion),
    path('giveans',views.GiveAnd),
]
