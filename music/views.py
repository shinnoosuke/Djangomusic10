from django.shortcuts import render,redirect
#from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView,UpdateView,DetailView
from .models import Teacher
from django.views import View
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

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
    fields = ("movie","fee","academic","experience","certificate","reputation","message","oneword","lang","teaching_inst","year","revel","pic","user_id")

    success_url = '/music/'

#class CreatePeopleView(CreateView):    
#    template_name = 'music/music_people_create.html'
#    model = User
#    fields = ("first_name","last_name","","city","introduction")

#    success_url = '/music/'


class DeleteMusicView(DeleteView):
    template_name = 'music/music_confirm_delete.html'
    model = Teacher
    success_url = '/music/'

def index_view(request):
    object_list = Teacher.objects.all()
    return render(request, 'music/index.html',{'object_list': object_list})


#def index_view(request):
#    object_list = Teacher.objects.all()
#    return render(request, 'music/index.html',{'object_list': object_list})

class UpdateMusicView(UpdateView): 
    model = Teacher
    fields = ("movie","fee","academic","experience","certificate","reputation","message","oneword","lang","inst","year","revel","pic","user_id")
    template_name = 'music/music_update.html'
    success_url = '/music/' 

class MypageView(View):
    def get(self, request, *args, **kwargs):

        print(request.user.id)

        context = {}
        context["teacher"] = Teacher.objects.filter(user_id=request.user.id).first()

        return render(request, "music/mypage.html",context)

    def post(self, request, *args, **kwargs):

        return redirect("mypage") 

class DirectMessageViewSet(ModelViewSet):
    queryset = DirectMessage.objects.all()
    serializer_class = DirectMessageSerializer

    def get_queryset(self):
        return self.queryset.filter(sender=self.request.user)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

    def destroy(self, request, *args, **kwargs):
        response = {'message': 'Delete DM is not allowed'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class InboxListView(ReadOnlyModelViewSet):
    queryset = DirectMessage.objects.all()
    serializer_class = DirectMessageSerializer

    def get_queryset(self):
        return self.queryset.filter(receiver=self.request.user)



#class CreateReviewView(CreateView):
#    model = Review
#    fields = ('teacher', 'title' , 'text' , 'rate')
#    template_name = 'teacher/review_form.html'     

#context_object_name = 'object_list'
#context_object_name = 'object_list'
