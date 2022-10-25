from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

class Skill(models.Model):
    Title = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.Title}"

class Tag(models.Model):
    Title = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.Title}"

class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    link = models.TextField()
    verified = models.BooleanField(default = False)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    image = models.CharField(max_length = 200)
    skills = models.ManyToManyField(Skill)
    points = models.IntegerField(default = 0)

class Company(models.Model):
    name = models.CharField(max_length = 20)

class Jobposting(models.Model):
    title = models.CharField(max_length = 30)
    job_description = models.FileField(upload_to = 'uploads/job_description/', validators=[FileExtensionValidator(allowed_extensions=["pdf"])])
    company = models.OneToOneField(Company, on_delete = models.CASCADE)

class Feedback(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    company = models.OneToOneField(Company, on_delete = models.CASCADE)
    rating = models.IntegerField()
    comments = models.TextField()