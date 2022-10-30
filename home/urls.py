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
    path('profileEdit/<int:profileId>', views.profileEdit, name = 'profile-edit'),
    path('jobPosting/<int:jobPostingId>', views.jobPosting, name = 'jobPosting'),
    path('createJobPosting/', views.createJobPosting, name = 'create-jobPosting'),
    path('editJobPosting/<int:jobPostingId>', views.editJobPosting, name = 'edit-jobPosting'),
    path('hire/<int:jobPostingId>/<int:userId>', views.hire, name = 'hire'),
    path('shell/', views.shell),
]
