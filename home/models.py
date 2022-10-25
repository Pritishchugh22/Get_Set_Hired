from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
    Title = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.Title}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    image = models.CharField(max_length = 200)
    skills = models.ManyToManyField(Skill, related_name='Skills')
    points = models.IntegerField(default = 0)