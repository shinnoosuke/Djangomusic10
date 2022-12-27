#from django.contrib.auth.models import User
#from django.urls import reverse_lazy
#from django.views.generic import CreateView

#from django.contrib.auth.models import User
#from django.urls import reverse_lazy
#from django.views.generic import CreateView

from .models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.shortcuts import render, redirect
from django.views import View
from .forms import SignupForm


#class SignupView(View):

#    def get(self,request,*args,**kwargs):
#        return render(request,"accounts/signup.html")

#    def post(self,request,*args,**kwargs):

#        form    = SignupForm(request.POST)

#        if form.is_valid():
#            form.save()

#        if request.POST["is_musician"]:
#            #TODO:音楽家であるにチェックが入っていた場合のリダイレクト先
#            return redirect()
#        else:
#            #TODO:音楽家であるにチェックが入ってなかった場合のリダイレクト先
#            return redirect()


class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'accounts/signup.html'

    def get_success_url(self) -> str:
        print(self.request.POST.get("is_musician",False))
        print(self.request)
        if self.request.POST.get("is_musician",False):
            #return reverse_lazy("music:musci-create")
            return reverse_lazy("/accounts/signup")
        else:
            print("---------")
            return reverse_lazy("music:index")





# class CreatePeopleView(CreateView):    
#    success_url = reverse_lazy('index')
#    template_name='people/User_account.html'
#    model= User
#    fields = ("first_name","last_name","email","city","introduction","image","is_musician")


#class SignupView(CreateView):
#    model = User
#    form_class = SignupForm
#    template_name = 'accounts/signup.html'
#    success_url = "/music/music_create.html"

class CreatePeopleView(CreateView):    
    success_url = reverse_lazy('index')
    template_name='people/User_account.html'
    model= User
    fields = ("first_name","last_name","email","city","introduction","image","is_musician")

#def receive_checkbox(request):
#    model = User
#    check = request.POST["is_musician"]
#    template_name = 'accounts/signup.html'
#    success_url = "/music/create.html"
