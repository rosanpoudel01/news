from django.urls import path
from useraccount.views import UserLoginView, SignupView
from django.contrib.auth.views import LogoutView

app_name = "user"

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", SignupView.as_view(), name="register"),
]
