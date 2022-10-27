def loginController(req):
    from django.contrib import messages
    from django.contrib.auth import authenticate, login
    username = req.POST['username']
    password = req.POST['password']
    user = authenticate(req, username=username, password=password)
    if user is not None:
        login(req, user)
        messages.success(req, f"{username} successfully loggedin!")
        context = {'status': True }
        return context

    messages.error(req, 'Please provide correct details.')
    context = {'status': False }
    return context


def registerController(req):
    # if req.method == 'POST':
    #     user_form = UserRegisterForm(req.POST)
    #     profile_form = ProfileRegisterForm(req.POST, req.FILES)
    #     if user_form.is_valid() and profile_form.is_valid():
    #         user_form.save()
    #         newusername = user_form.cleaned_data.get('username')
    #         newuser = User.objects.filter(username=newusername).first()

    #         profile_form = ProfileRegisterForm(
    #             req.POST, req.FILES, instance=newuser.profile)
    #         profile_form.save()

    #         messages.success(req, f"Account created for {newusername}!")
    #         return redirect('login')
    #     else:
    #         messages.error(req, 'Please correct the error below.')
    # else:
    #     user_form = UserRegisterForm()
    #     profile_form = ProfileRegisterForm()

    # context = {
    #     'title': 'Register',
    #     'user_form': user_form,
    #     'profile_form': profile_form
    # }

    # return render(req, 'users/signup.html', context)

    # if (req.method == 'POST'):
    #     return True
    # return False
    pass


def indexController(req):
    from home.models import Jobposting
    jobPostings = Jobposting.objects.all()
    context = {"status": True, "image": req.user.profile.image, "jobs": jobPostings}
    return context
