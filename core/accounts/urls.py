from django.urls import path
from .views import *


urlpatterns = [
    path("login/", user_login, name="login"),
    path("signup/", user_signup, name="signup"),
    path("logout/", user_logout, name="logout"),
    path("profile/", user_profile, name="profile"),
    path("update/", update_profile, name="update"),
]