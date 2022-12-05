#from django.urls import path

#from .migrations import views
from . import views

from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

    path('music/', views.ListMusicView.as_view()),
    path('music/create/', views.CreateMusicView.as_view()),

    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
