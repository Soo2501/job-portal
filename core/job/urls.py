from django.urls import path
from .views import *

urlpatterns = [
    path("jobs/add/", job_form, name="add-job"),
    path("category/", category, name="category"),
    path("jobs/detail/<int:id>/", job_detail, name="detail"),
    path("jobs/apply/<int:id>/", job_apply, name="apply"),
]