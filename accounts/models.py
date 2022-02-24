from wsgiref.validate import validator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

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
    judges_assigned = models.ManyToManyField(User)
    validator = [ MinValueValidator(0), MaxValueValidator(100)]

    def __str__(self):
        return self.title + " by " + self.team_name
    
    def total(self):
        judgements = Judgement.objects.filter(submission = self)
        tot = 0
        for j in judgements:
            tot = tot + j.total()             
        return tot
    
    def Judge1(self):
        judges = self.judges_assigned.all() 
        return judges[0].username

    def Judge2(self):
       judges = self.judges_assigned.all() 
       return judges[1].username

    def judge_1_marks(self):
        judgements = Judgement.objects.filter(submission = self).first()
        return str(judgements.param1) + ", " + str(judgements.param2) + ", " + str(judgements.param3)
    
    def judge_1_total(self):
        judgements = Judgement.objects.filter(submission = self).first()
        return judgements.total()

    def judge_2_marks(self):
        judgements = Judgement.objects.filter(submission = self).last()   
        return str(judgements.param1) + ", " + str(judgements.param2) + ", " + str(judgements.param3)
    
    def judge_2_total(self):
        judgements = Judgement.objects.filter(submission = self).last()   
        return judgements.total()
    
class Judgement(models.Model):
    judge = models.ForeignKey(User, models.CASCADE)
    submission = models.ForeignKey(Submissions, on_delete=models.CASCADE)
    validator = [ MinValueValidator(0), MaxValueValidator(100)]
    param1 = models.IntegerField(validators=validator , default=0)
    param2 = models.IntegerField(validators=validator, default=0)
    param3 = models.IntegerField(validators=validator, default=0)


    def total(self):
        return self.param1 + self.param2 + self.param3
