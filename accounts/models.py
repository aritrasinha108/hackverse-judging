from wsgiref.validate import validator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ObjectDoesNotExist
# Create your models here.

class User(AbstractUser):
    is_organiser = models.BooleanField(default=False)
    
class Submissions(models.Model):
    title = models.CharField(blank=False, max_length=200)
    description = models.TextField(blank=False)
    devfolio_link = models.URLField(blank=False)
    codebase_link = models.URLField(blank=False)
    team_name = models.CharField(blank=False, max_length=30)
    primary_track = models.CharField(blank=True, max_length=200)
    secondary_track = models.CharField(blank=True, max_length=200)
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
        judge1 = "Not Assigned"
        judges = self.judges_assigned.all() 
        judge1 = judges[0].username
        return judge1

    def Judge2(self):
        judge2 = "Not Assigned"
        judges = self.judges_assigned.all() 
        judge2 = judges[1].username
        return judge2


    def judge_1_marks(self):
        marks = "Not marked" 
        judgements = Judgement.objects.filter(submission = self).first()
        if judgements:
            marks = str(judgements.param1) + ", " + str(judgements.param2) + ", " + str(judgements.param3) + ", " + str(judgements.param4) + ", " + str(judgements.param5)
        return marks

    def judge_1_total(self):
        tot =0
        judgements = Judgement.objects.filter(submission = self).first()
        if judgements:
            tot += judgements.total()
        return tot

    def judge_2_marks(self):
        marks = "Not marked" 
        judgements = Judgement.objects.filter(submission = self).last()
        if judgements:
            marks = str(judgements.param1) + ", " + str(judgements.param2) + ", " + str(judgements.param3) + ", " + str(judgements.param4) + ", " + str(judgements.param5)
        return marks

    
    def judge_2_total(self):
        tot =0
        judgements = Judgement.objects.filter(submission = self).last()
        if judgements:
            tot += judgements.total()
        return tot

    
    def marked(self):
        try:
            judgements = self.judgement_set.count()
            return judgements
        except ObjectDoesNotExist:
            return 0
class Judgement(models.Model):
    judge = models.ForeignKey(User, models.CASCADE)
    submission = models.ForeignKey(Submissions, on_delete=models.CASCADE)
    validator1 = [ MinValueValidator(0), MaxValueValidator(10)]
    validator2 = [ MinValueValidator(0), MaxValueValidator(20)]
    param1 = models.IntegerField(validators=validator1 , default=0, verbose_name="ORIGINALITY OF IDEA/ ADVANCEMENTS IN THE FIELD")
    param2 = models.IntegerField(validators=validator1, default=0, verbose_name="BUSINESS VALUE / SOCIETAL IMPACT")
    param3 = models.IntegerField(validators=validator2, default=0, verbose_name="IMPLEMENTATION OF IDEA")
    param4 = models.IntegerField(validators=validator1, default=0, verbose_name="QUALITY OF PRESENTATION")
    param5 = models.IntegerField(validators=validator1, default=0, verbose_name="RELEVANCE TO PRIMARY TRACKS")
    param6 = models.IntegerField(validators=validator1, default=0, verbose_name="RELEVANCE TO SECONDARY TRACK")


    def total(self):
        return self.param1 + self.param2 + self.param3 + self.param4
