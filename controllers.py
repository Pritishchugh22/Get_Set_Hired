from django.contrib import messages
from utils import sendFormErrorMessages

def loginController(req):
    from django.contrib.auth import authenticate, login
    username = req.POST['username']
    password = req.POST['password']
    user = authenticate(req, username=username, password=password)
    if user is not None:
        login(req, user)
        messages.success(req, f"{username} successfully loggedin!")
        context = {'status': True}
        return context

    messages.error(req, 'Please provide correct details.')
    context = {'status': False}
    return context


def userRegisterController(req):
    from home.forms import UserRegisterForm
    from django.contrib.auth.models import User

    form = UserRegisterForm(req.POST)
    if form.is_valid():
        form.save()

        username = form.cleaned_data.get('username')
        user = User.objects.get(username=username)
        user.userprofile.isUser = True
        user.userprofile.save()

        messages.success(req, f"Account created for {username}!")
        context = {"status": True}
        return context

    sendFormErrorMessages(req, form)
    context = {"status": False}
    return context


def companyRegisterController(req):
    from home.forms import CompanyRegisterForm
    from django.contrib.auth.models import User

    form = CompanyRegisterForm(req.POST)
    if form.is_valid():
        form.save()

        username = form.cleaned_data.get('username')
        user = User.objects.get(username=username)
        user.companyprofile.isCompany = True
        user.companyprofile.save()

        messages.success(req, f"Account created for {username}!")
        context = {"status": True, "form": form}
        return context

    sendFormErrorMessages(req, form)
    context = {"status": False, "form": form}
    return context


def indexController(req):
    from home.models import Jobposting
    jobPostings = Jobposting.objects.all()
    context = {"status": True,
               "image": req.user.userprofile.image, "jobs": jobPostings}
    return context


def profileEditController(req, profileId):
    if req.method == "POST":
        from utils import tryExcept
        from home.models import UserProfile, CompanyProfile

        profile = UserProfile.objects.get(id=profileId)
        if profile == None:
            profile = CompanyProfile.objects.get(id=profileId)
        user = profile.user
        username = user.username

        tryExcept(user, req.POST, 'first_name')
        tryExcept(user, req.POST, 'last_name')
        tryExcept(user, req.POST, 'email')
        user.save()

        messages.success(req, f"Profile updated for {username}!")
        context = {"status": True}
        return context

    context = {"status": True, "user": req.user}
    return context
