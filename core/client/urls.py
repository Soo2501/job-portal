from django.urls import path
from .views import *


urlpatterns = [
    path("",home,name="home"),
    path("profile/add/", add_edu, name="add-edu"),
    path("profile/<id>/", data_delete, name="delete"),
    path("profile/edit/<id>/", edit_data, name="edit"),
]