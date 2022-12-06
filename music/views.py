from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView,UpdateView,DetailView
from .models import Teacher


class ListMusicView(ListView):
    template_name = 'music_list.html'
    model = Teacher
    #model = music 

class DetailMusicView(DetailView):
    template_name = 'music/music_detail.html'
    model = Teacher     

class CreateMusicView(CreateView):    
    template_name = 'music/music_create.html'
    model = Teacher
    fields = ("movie","fee","academic","experience","certificate","reputation","message","oneword","lang","inst","pic","user_id")

    success_url = '/music/'

class DeleteMusicView(DeleteView):
    template_name = 'music/music_confirm_delete.html'
    model = Teacher
    success_url = '/music/'

class UpdateMusicView(UpdateView): 
    model = Teacher
    fields = ("movie","fee","academic","experience","certificate","reputation","message","oneword","lang","inst","pic","user_id")
    template_name = 'music/music_update.html'
    success_url = '/music/'  

#context_object_name = 'object_list'
#context_object_name = 'object_list'
