from django.urls import path

#from .migrations import views
from . import views

urlpatterns = [

    path('music/', views.ListMusicView.as_view()),
    path('music/create/', views.CreateMusicView.as_view()),

    
]
