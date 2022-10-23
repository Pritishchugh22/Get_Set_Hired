from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(req):
    print(req.user)
    return render(req, 'home/index.html')