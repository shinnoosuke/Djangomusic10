#from django.urls import path

#from .migrations import views
from . import views

from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

    path('music/', views.ListMusicView.as_view()),
    path('music/<int:pk>/detail/', views.DetailMusicView.as_view()),
    #path('music/detail/', views.DetailMusicView.as_view()),
    path('music/create/', views.CreateMusicView.as_view()),
    path('music/<int:pk>/delete/', views.DeleteMusicView.as_view(), name='delete-music'),
    path('music/<int:pk>/update/', views.UpdateMusicView.as_view(), name='update-music'),
    #path('music/<int:music_id>/review/', views.CreateReviewView.as_View(),name='review'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
