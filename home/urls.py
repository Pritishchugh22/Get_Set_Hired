from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name = 'index'),
    path('main/', views.main, name = 'main'),
    path('login/', views.login, name = 'login'),
    path('register/', views.register, name = 'register'),
    path('userRegister/', views.userRegister, name = 'user-register'),
    path('companyRegister/', views.companyRegister, name = 'company-register'),
    path('profile/<int:profileId>', views.profile, name = 'profile'),
    path('profile_c/<int:profileId>', views.profile_c, name = 'company-profile'),
    path('profileEdit/<int:profileId>', views.profileEdit, name = 'profile-edit'),
    path('jobPosting/<int:jobPostingId>', views.jobPosting, name = 'jobPosting'),
    path('createJobPosting/', views.createJobPosting, name = 'create-jobPosting'),
    path('editJobPosting/<int:jobPostingId>', views.editJobPosting, name = 'edit-jobPosting'),
    path('shell/', views.shell),
]
