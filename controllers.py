from django.contrib import messages
from utils import sendFormErrorMessages, tryExcept
from home.models import Notification

def shellController():
    from home.models import Tag, Skill
    count = len(Tag.objects.all())
    tag = Tag(title = 'tag' + str(count+1))
    tag.save()

    count = len(Skill.objects.all())
    skill = Skill(title = 'tag' + str(count+1))
    skill.save()

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
    context = {"status": True}
    from home.models import Notification 
    if req.user.userprofile.isUser:
        context["image"] = req.user.userprofile.image
    else:
        from home.models import JobPosting
        jobPostings_closed = JobPosting.objects.all().filter(status = 'closed')
        jobPostings_open = JobPosting.objects.all().filter(status = 'open')
        context["jobPostings_open"] = jobPostings_open
        context["jobPostings_closed"] = jobPostings_closed
    context["notifications"] = Notification.objects.filter(reciever = req.user).order_by('-time')
    return context


def profileController(req, profileId):
    from home.models import UserProfile, CompanyProfile
    import requests

    user = True
    profile = UserProfile.objects.get(id=profileId)
    if profile.isUser == False:
        user = False
        profile = CompanyProfile.objects.get(id=profileId)

    context = {"status": True, "user": profile.user, "profile": profile}
    if user == False:
        context['website'] = requests.get(profile.website_link).text
        print(context['website'])
    # print(context)
    return context


def profileEditController(req, profileId):
    from utils import profileCompleted
    if req.method == "POST":
        from utils import tryExcept
        from home.models import UserProfile, CompanyProfile
        from home.forms import UpdateUserProfileForm

        profile = UserProfile.objects.get(id=profileId)
        if profile == None:
            profile = CompanyProfile.objects.get(id=profileId)
        user = profile.user
        username = user.username

        data = req.POST.dict()
        for key in data:
            tryExcept(req, user, key, data[key])
        user.save()
        data['user'] = user
        print(data)
        if user.userprofile.isUser:
            form = UpdateUserProfileForm(data, req.FILES, instance = profile)
            if form.is_valid():
                form.save()
                messages.success(req, f"Profile updated for {username}!")
                context = {"status": True}
                return context
            sendFormErrorMessages(req, form)
            context = {"status": False}
            return context
        else:
            user.companyprofile.email = data['email']
            user.companyprofile.name = data['name']
            user.companyprofile.contact_num = data['contact_num']
            user.companyprofile.number_of_employees = data['number_of_employees']
            user.companyprofile.website_link = data['website_link']
            user.companyprofile.save()
            messages.success(req, f"Profile updated for {username}!")
            context = {"status": True}
            return context

    context = {"status": True, "user": req.user}
    if not profileCompleted(req):
        context['showNav'] = False
    return context

def jobPostingController(req, jobPostingId):
    from home.models import JobPosting, UserProfile

    jobposting = JobPosting.objects.get(id = jobPostingId)
    users = UserProfile.objects.all().filter(isUser = True)
    users_accepted = jobposting.users_accepted.all()
    willing_to_hire_users = list(jobposting.willing_to_hire.all())
    willing_to_hire_users = [user.userprofile for user in willing_to_hire_users]
    rem_users = [user for user in users if user not in willing_to_hire_users]
    context = {"status": True, "users_accepted":users_accepted, "jobPosting": jobposting, "willing_to_hire_users": willing_to_hire_users, 'rem_users': rem_users}
    return context

def createJobPostingController(req):
    from home.forms import CreateJobPostingForm
    if req.method == "POST":
        data = req.POST.dict()
        domain_tags = req.POST.getlist('domain_tags')
        requirement_tags = req.POST.getlist('requirement_tags')
        data['domain_tags'] = domain_tags
        data['requirement_tags'] = requirement_tags
        data['company'] = req.user
        form = CreateJobPostingForm(data, req.FILES)
        if form.is_valid():
            jobposting = form.save()
            req.user.companyprofile.jobpostings.add(jobposting)
            messages.success(req, f"JobPosting created successfully!")
            context = {"status": True, 'jobPostingId': jobposting.pk}
            return context

        sendFormErrorMessages(req, form)
        context = {"status": False, "jobPostingForm": CreateJobPostingForm()}
        return context
    context = {"status": True, "jobPostingForm": CreateJobPostingForm()}
    return context

def editJobPostingController(req, jobPostingId):
    from home.models import JobPosting
    from home.forms import EditJobPostingForm
    jobPosting = JobPosting.objects.get(id = jobPostingId)
    if req.method == "POST":
        data = req.POST.dict()
        domain_tags = req.POST.getlist('domain_tags')
        requirement_tags = req.POST.getlist('requirement_tags')
        data['domain_tags'] = domain_tags
        data['requirement_tags'] = requirement_tags
        data['company'] = req.user

        form = EditJobPostingForm(data, req.FILES, instance = jobPosting)
        if form.is_valid():
            form.save()

            messages.success(req, f"JobPosting successfully updated!")
            context = {"status": True}
            return context
        sendFormErrorMessages(req, form)
        context = {"status": False}
        return context

    context = {"status": True, "jobPostingForm": EditJobPostingForm(instance = jobPosting)}
    return context

def giveFeedbackController(req, companyId, userId):
    pass

def hireController(req, jobPostingId, userId):
    from home.models import JobPosting
    from django.contrib.auth.models import User
    from utils import sendNotification

    user = User.objects.get(id = userId)
    jobposting = JobPosting.objects.get(id = jobPostingId)
    jobposting.willing_to_hire.add(user)
    jobposting.save()

    sendNotification(jobposting, user, "Want this job?")
