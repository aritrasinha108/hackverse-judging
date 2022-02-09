from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_organiser = models.BooleanField(default=False)

class Submissions(models.Model):
    title = models.CharField(blank=False, max_length=200)
    description = models.TextField(blank=False)
    devfolio_link = models.URLField(blank=False)
    codebase_link = models.URLField(blank=False)
    team_name = models.CharField(blank=False, max_length=30)
    member_name = models.CharField(blank=False, max_length=30)
    member_email = models.EmailField()
    member_phone = models.CharField(max_length=13)
    

    def __str__(self):
        return self.title + " by " + self.team_name

