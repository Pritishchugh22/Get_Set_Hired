from django.contrib import admin
from .models import Skill, Tag, Certificate, Jobposting, Message, Feedback, Profile, Company, Room

admin.site.register(Skill)
admin.site.register(Tag)
admin.site.register(Certificate)
admin.site.register(Jobposting)
admin.site.register(Message)
admin.site.register(Feedback)

admin.site.register(Profile)
admin.site.register(Company)
admin.site.register(Room)
