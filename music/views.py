from django.shortcuts import render
from django.views.generic import ListView
from .models import Teacher


class ListMusicView(ListView):
    template_name = 'music_list.html'
    model = Teacher
    #model = music  
    
context_object_name = 'object_list'
#context_object_name = 'object_list'
