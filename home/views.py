from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from controllers import *
from home.decorators import *

@user_is_not_logged_in
def main(req):
        return render(req, 'home/main.html')

@user_is_not_logged_in
def login(req):
    if req.method == 'POST':
        context = loginController(req)
        if context['status']:
            return redirect('/')
        return redirect('/login/')
    return render(req, 'home/login.html')

@user_is_not_logged_in
def register(req):
    return render(req, 'home/register.html')

@user_is_not_logged_in
def userRegister(req):
    if req.method == 'POST':
        context = userRegisterController(req)
        if context['status']:
            return redirect('index')
    return redirect('/register')

@user_is_not_logged_in
def companyRegister(req):
    if req.method == 'POST':
        context = companyRegisterController(req)
        if context['status']:
            return redirect('index')
    return redirect('/register')

@login_required
@user_profile_completed
def index(req):
    context = indexController(req)
    return render(req, 'home/index.html', context)

@login_required
def profileEdit(req, profileId):
    context = profileEditController(req, profileId)
    if req.method == 'POST':
        return redirect('index')
    return render(req, 'home/profileEdit.html', context)

@user_passes_test(lambda u: u.is_superuser)
def shell(req):
    # req.user.userprofile.isUser = True
    # req.user.userprofile.save()
    return redirect('index')
