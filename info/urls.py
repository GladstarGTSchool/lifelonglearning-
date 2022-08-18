from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('learner/', views.learner, name="learner"),
    path('teacher/', views.teacher, name="teacher"),
    path('informant/', views.informant, name="informant"),


    ]
