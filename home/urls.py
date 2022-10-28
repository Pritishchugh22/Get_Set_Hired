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
    path('createJobPosting/', views.createJobPosting, name = 'create-job-posting'),
    path('editJobPosting/<int:jobPostingId>', views.editJobPosting, name = 'edit-job-posting'),
    path('shell/', views.shell),
]
