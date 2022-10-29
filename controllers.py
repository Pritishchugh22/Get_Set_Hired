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
    if req.user.userprofile.isUser:
        context["image"] = req.user.userprofile.image
    else:
        from home.models import JobPosting
        jobPostings = JobPosting.objects.all()
        context["jobPostings"] = jobPostings
    context["notifications"] = Notification.objects.filter(reciever = req.user).order_by('-time'),
    return context


def profileController(req, profileId):
    from home.models import UserProfile, CompanyProfile

    profile = UserProfile.objects.get(id=profileId)
    if profile == None:
        profile = CompanyProfile.objects.get(id=profileId)

    context = {"status": True, "user": req.user, "profile": profile}
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
            user.companyprofile.save()
            messages.success(req, f"Profile updated for {username}!")
            context = {"status": True}
            return context

    context = {"status": True, "user": req.user}
    if not profileCompleted(req):
        context['showNav'] = False
    return context

def jobPostingController(req, jobPostingId):
    from home.models import JobPosting
    jobPosting = JobPosting.objects.get(id = jobPostingId)
    context = {"status": True, "jobPosting": jobPosting}
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
        print(data)
        form = CreateJobPostingForm(data, req.FILES)
        print(form)
        if form.is_valid():
            jobPosting = form.save()

            messages.success(req, f"JobPosting created successfully!")
            context = {"status": True, 'jobPostingId': jobPosting.pk}
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