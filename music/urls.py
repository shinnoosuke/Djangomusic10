from django.urls import path

from .migrations import views


urlpatterns = [

    path('music/', views.ListMusicView.as_view()),
    
]
