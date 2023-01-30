from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from useraccount.forms import UserSignupForm

# Create your views here.
User = get_user_model()


class UserLoginView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True


class SignupView(CreateView):
    model = User
    form_class = UserSignupForm
    template_name = "register.html"
    success_url = reverse_lazy("news:news")
