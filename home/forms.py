from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from home.models import JobPosting, UserProfile, CompanyProfile
from django.forms import ModelForm

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class CompanyRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CreateJobPostingForm(ModelForm):
    class Meta:
        model = JobPosting
        fields = '__all__'

class UpdateUserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user', 'image', 'contact_num', 'education', 'experience_yrs', 'age', 'willing_to_work_at')
