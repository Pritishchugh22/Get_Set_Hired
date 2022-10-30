from django.contrib import admin
from .models import Skill, Tag, Certificate, JobPosting, Message, Feedback, UserProfile, CompanyProfile, Room, Notification

admin.site.register(Skill)
admin.site.register(Tag)
admin.site.register(Certificate)
admin.site.register(JobPosting)
admin.site.register(Message)
admin.site.register(Feedback)

admin.site.register(UserProfile)
admin.site.register(CompanyProfile)
admin.site.register(Room)
admin.site.register(Notification)
