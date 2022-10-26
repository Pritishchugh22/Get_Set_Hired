from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from home.models import Jobposting

@login_required
def index(req):
    jobPostings = Jobposting.objects.all()
    context = {"image": req.user.profile.image, "jobs": jobPostings}
    return render(req, 'home/index.html', context)