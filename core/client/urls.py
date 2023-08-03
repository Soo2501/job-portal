from django.urls import path
from .views import *


urlpatterns = [
    path("",home,name="home"),
    path("search/", search_data, name="search"),
    path("profile/add/", add_edu, name="add-edu"),
    path("profile/add/training/", add_tra, name="add-train"),
    path("profile/<id>/", data_delete, name="delete"),
    path("profile/<id>/data/", train_delete, name="train-delete"),
    path("profile/edit/<id>/", edit_data, name="edit"),
    path("profile/add/skills/", add_skills, name="skills"),
    path("profile/add/cv/", add_cv, name="cv"),
    path("profile/cv/<int:id>/", edit_cv, name="editcv"),
    path("profile/add/language/", add_language, name="language"),
]