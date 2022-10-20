from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def login(request):
    return render(request, 'authentication/login.html')

@login_required
def index(req):
    return render(req, 'home/index.html')