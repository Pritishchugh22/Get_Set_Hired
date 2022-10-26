from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
import django

class Skill(models.Model):
    title = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.title}"

class Tag(models.Model):
    title = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.title}"

class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    link = models.TextField(blank = False)
    verified = models.BooleanField(default = False)
    def __str__(self):
        return f"{self.link}"

class Jobposting(models.Model):
    title = models.CharField(max_length = 40)
    job_description = models.FileField(upload_to = 'uploads/job_description/', validators=[FileExtensionValidator(allowed_extensions=["pdf"])])
    company = models.OneToOneField('home.Company', on_delete = models.CASCADE, related_name = 'jobposting_company')
    users_accepted = models.ManyToManyField(User)
    def __str__(self):
        return f"{self.title}"

class Message(models.Model):
    content = models.TextField(blank=False)
    time = models.DateTimeField(default = django.utils.timezone.now)
    def __str__(self):
        return f"{self.content}"

class Feedback(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    company = models.OneToOneField('home.Company', on_delete = models.CASCADE, related_name = 'feedback_company')
    rating = models.IntegerField(blank=False)
    comments = models.TextField()
    def __str__(self):
        return f"{self.rating}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    certificates = models.ManyToManyField(Certificate)
    image = models.CharField(max_length = 200)
    skills = models.ManyToManyField(Skill)
    points = models.IntegerField(default = 0)
    def __str__(self):
        return f"{self.user}"

class Company(models.Model):
    name = models.CharField(max_length = 40)
    jobpostings = models.ManyToManyField(Jobposting, related_name = 'job_posting', blank = True)
    def __str__(self):
        return f"{self.name}"
class Room(models.Model):
    room_name = models.CharField(max_length = 30, unique = True)
    user = models.ManyToManyField(User)
    company = models.ManyToManyField(Company)
    messages = models.ManyToManyField(Message)
    start_time = models.DateTimeField(default = django.utils.timezone.now)
    def __str__(self):
        return f"{self.room_name}"