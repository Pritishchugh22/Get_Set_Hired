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
    link = models.TextField()
    verified = models.BooleanField(default = False)
    def __str__(self):
        return f"{self.link}"

class JobPosting(models.Model):
    title = models.CharField(max_length = 40)
    position = models.CharField(max_length = 40)
    job_description = models.FileField(upload_to = 'job_description/', validators=[FileExtensionValidator(allowed_extensions=["pdf"])])
    company = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'jobposting_company')
    users_accepted = models.ManyToManyField(User, related_name = 'users_accepted', blank=True)
    no_of_seats = models.IntegerField()
    stipend = models.IntegerField()
    location = models.CharField(max_length = 40)
    domain_tags = models.ManyToManyField(Tag, related_name = 'jobposting_domain_tags')
    requirement_tags = models.ManyToManyField(Tag, related_name = 'jobposting_requirement_tags')
    status = models.CharField(max_length = 10, choices = (("open", "open"), ("closed", "closed")), default = 'open')
    experience_required = models.IntegerField(default = 0)
    willing_to_hire = models.ManyToManyField(User, related_name = 'users_willing_to_hire', blank = True)
    def __str__(self):
        return f"{self.title}"

class Message(models.Model):
    content = models.TextField()
    time = models.DateTimeField(default = django.utils.timezone.now)
    def __str__(self):
        return f"{self.content}"

class Feedback(models.Model):
    user = models.ManyToManyField(User, related_name = 'feedback_user')
    company = models.ManyToManyField(User, related_name = 'feedback_company')
    rating = models.IntegerField()
    comments = models.TextField()
    def __str__(self):
        return f"{self.rating}"


class UserProfile(models.Model):
    isUser = models.BooleanField(default = False)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    certificates = models.ManyToManyField(Certificate, related_name = 'user_certificates')
    image = models.FileField(upload_to = 'images/', validators=[FileExtensionValidator(allowed_extensions=["png", "jpg", "jpeg"])])
    skills = models.ManyToManyField(Skill, related_name = 'user_skills')
    contact_num = models.IntegerField('Contact Number')
    education = models.TextField()
    experience_yrs = models.IntegerField(default = 0)
    age = models.IntegerField()
    willing_to_work_at = models.CharField(max_length = 40)
    def __str__(self):
        return f"{self.user}"

class CompanyProfile(models.Model):
    isCompany = models.BooleanField(default = False)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    jobpostings = models.ManyToManyField(JobPosting, related_name = 'job_postings', blank = True)
    name = models.CharField(max_length = 40)
    contact_num = models.IntegerField('Contact Number')
    number_of_employees = models.IntegerField()
    def __str__(self):
        return f"{self.user}"

class Room(models.Model):
    room_name = models.CharField(max_length = 30, unique = True)
    users = models.ManyToManyField(User, related_name = 'room_users')
    companies = models.ManyToManyField(User, related_name = 'room_companies')
    messages = models.ManyToManyField(Message)
    start_time = models.DateTimeField(default = django.utils.timezone.now)
    def __str__(self):
        return f"{self.room_name}"

class Notification(models.Model):
    sender = models.ManyToManyField(User, related_name = 'notification_sender')
    reciever = models.ManyToManyField(User, related_name = 'notification_reciever')
    message = models.TextField()
    time = models.DateTimeField(default = django.utils.timezone.now)
    jobposting = models.ForeignKey(JobPosting, on_delete = models.CASCADE)
    def __str__(self):
        return f"{self.message}"