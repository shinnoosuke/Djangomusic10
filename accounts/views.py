#from django.contrib.auth.models import User
#from django.urls import reverse_lazy
#from django.views.generic import CreateView

from .models import User, Review
from django.urls import reverse_lazy
from django.views.generic import CreateView


from .forms import SignupForm


class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'accounts/signup.html'
    success_url = "/accounts/create"

class CreatePeopleView(CreateView):    
    success_url = reverse_lazy('index')
    template_name='people/User_account.html'
    model= User
    fields = ("first_name","last_name","email","city","introduction","image","is_musician")

class CreateReviewView(CreateView):
    model = Review
    fields = ('title', 'text', 'rate')
    template_name ='accounts/review_form.html'    


