from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from controllers import *
from home.decorators import user_is_not_logged_in

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
def index(req):
    context = indexController(req)
    return render(req, 'home/index.html', context)

@user_is_not_logged_in
def main(req):
        return render(req, 'home/main.html')