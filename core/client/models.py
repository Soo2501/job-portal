from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Cv(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="cv")


    def __str__(self):
        return self.user.username