from django.contrib import admin
from .models import Submissions, User

# Register your models here.

admin.site.register(User)
admin.site.register(Submissions)