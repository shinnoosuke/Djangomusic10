from django.shortcuts import render
from django.views.generic import ListView
from accounts.models import User


class ListMusicView(ListView):
    template_name = 'music/music_list.html'
    model = User


# Create your views here.
