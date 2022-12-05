from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Teacher


class ListMusicView(ListView):
    template_name = 'music_list.html'
    model = Teacher
    #model = music  

#class CreatMusicView(CreateView):
class CreateMusicView(CreateView):    
    template_name = 'music/music_create.html'
    model = Teacher
    fields = ('fee','academic','certificate')

#context_object_name = 'object_list'
#context_object_name = 'object_list'
