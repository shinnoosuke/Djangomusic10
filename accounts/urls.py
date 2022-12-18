from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .import views
from .views import SignupView, CreatePeopleView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('accounts/create/', views.CreatePeopleView.as_view()),
]