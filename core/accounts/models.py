from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile = models.ImageField(upload_to="profile_images", default="xyz.jpg", null=False, blank=False)
    birthdate = models.DateField(null=True, blank=False)
    phone = models.CharField(max_length=10, null=False, blank=False)
    phone1 = models.CharField(max_length=10, null=True, blank=True)
    Address = models.CharField(max_length=120, null=False, blank=False)

    def __str__(self):
        return self.user.username

class Education(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, null=False, blank=False)
    degree = models.CharField(max_length=120, null=False, blank=False)
    school_name = models.CharField(max_length=120, null=False, blank=False)
    date = models.DateField(auto_now=True)
    gpa = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.FileField(upload_to="certificates")

    def __str__(self):
        return self.user.username

class Training(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, null=False, blank=False)
    starting_date = models.DateField(auto_now=True)
    ending_date = models.DateField(auto_now=True)
    institute_name = models.CharField(max_length=120, null=False, blank=False)
    image = models.FileField(upload_to="certificates", null=False)

    def __str__(self):
        return self.user.username

class Documents(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    ctz_front = models.FileField(upload_to="documents", null=False)
    ctz_back = models.FileField(upload_to="documents", null=False)
    liscence = models.FileField(upload_to="documents", null=True )

    def __str__(self):
        return self.user.username

class Skills(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    skills = models.TextField(null=False, blank=False)
    language = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.user.username