from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Education)
admin.site.register(Training)
admin.site.register(Documents)
admin.site.register(Skills)