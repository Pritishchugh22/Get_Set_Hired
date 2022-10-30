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
@user_profile_completed
@can_check_profile
def profile(req, profileId):
    context = profileController(req, profileId)
    return render(req, 'home/profile.html', context)

@login_required
@is_user_profile
def profileEdit(req, profileId):
    context = profileEditController(req, profileId)
    if req.method == 'POST':
        return redirect('index')
    return render(req, 'home/profileEdit.html', context)

@login_required
@user_profile_completed
def jobPosting(req, jobPostingId):
    context = jobPostingController(req, jobPostingId)
    return render(req, 'home/jobPosting.html', context)

@login_required
@user_passes_test(lambda u: u.companyprofile.isCompany == True)
@user_profile_completed
def createJobPosting(req):
    context = createJobPostingController(req)
    if req.method == 'POST' and context['status']:
        return redirect('jobPosting', context['jobPostingId'])
    return render(req, 'home/createJobPosting.html', context)

@login_required
@user_passes_test(lambda u: u.companyprofile.isCompany == True)
@user_profile_completed
# company is job creator
def editJobPosting(req, jobPostingId):
    context = editJobPostingController(req, jobPostingId)
    if req.method == 'POST':
        return redirect('jobPosting', jobPostingId)
    return render(req, 'home/editJobPosting.html', context)

@login_required
@user_passes_test(lambda u: u.companyprofile.isCompany == True)
@user_profile_completed
def hire(req, jobPostingId, userId):
    context = hireController(req, jobPostingId, userId)
    return redirect('/jobPosting/' +str(jobPostingId), context)

@login_required
@user_passes_test(lambda u: u.companyprofile.isCompany == True)
@user_profile_completed
def giveFeedback(req, companyId, userId):
    context = giveFeedbackController(req, companyId, userId)
    return redirect('/profile/{userId}')

@user_passes_test(lambda u: u.is_superuser)
def shell(req):
    from controllers import shellController
    shellController()
    return redirect('index')