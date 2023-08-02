from django.urls import path
from .views import *


urlpatterns = [
    path("",home,name="home"),
    path("profile/add/", add_edu, name="add-edu"),
    path("profile/add/training/", add_tra, name="add-train"),
    path("profile/<id>/", data_delete, name="delete"),
    path("profile/<id>/data/", train_delete, name="train-delete"),
    path("profile/edit/<id>/", edit_data, name="edit"),
    path("profil/add/skills/", add_skills, name="skills"),
    path("profil/add/language/", add_language, name="language"),
]