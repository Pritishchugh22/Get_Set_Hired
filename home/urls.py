from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name = 'index'),
    path('login/', views.login, name = 'login'),
    path('register/', views.register, name = 'register'),
    path('userRegister/', views.userRegister, name = 'user-register'),
    path('companyRegister/', views.companyRegister, name = 'company-register'),
]
