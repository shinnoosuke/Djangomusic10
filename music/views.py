from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView,UpdateView,DetailView
from .models import Teacher
from django.views import View


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

#def index_view(request):
#    return render(request, 'music/index.html,{'somedata': 100})

class UpdateMusicView(UpdateView): 
    model = Teacher
    fields = ("movie","fee","academic","experience","certificate","reputation","message","oneword","lang","inst","pic","user_id")
    template_name = 'music/music_update.html'
    success_url = '/music/' 

class MypageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "music/mypage.html")

    def post(self, request, *args, **kwargs):
        return redirect("mypage") 

        #print(request.user.id)





#class CreateReviewView(CreateView):
#    model = Review
#    fields = ('teacher', 'title' , 'text' , 'rate')
#    template_name = 'teacher/review_form.html'     

#context_object_name = 'object_list'
#context_object_name = 'object_list'
