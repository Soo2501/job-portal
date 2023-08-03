from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Job(models.Model):
    job = [
        ("fulltime","fulltime"),
        ("parttime","parttime"),
        ("contract","contract"),
        ("internship","internship")
    ]
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 120, null=False, blank=False)
    company = models.CharField(max_length = 120, null=False, blank=False)
    location = models.CharField(max_length = 120, null=False, blank=False)
    jtype = models.CharField(max_length=120, choices=job)
    desc = models.TextField(null=False, blank=False)
    requirements = models.TextField(null=False, blank=False)
    wsite = models.CharField(max_length=120, null=False, blank=False)
    deadline = models.DateField()


    def __str__(self):
        return self.title +"--"+ self.user.username

    class Meta:
        ordering = ["-id"]