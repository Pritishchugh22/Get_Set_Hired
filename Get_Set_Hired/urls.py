from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls.conf import include
# from users import views as users_views
# from django.conf import settings
# from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('', include('home.urls')),
    # path('accounts/', include('allauth.urls')),
    # path('oauth/', users_views.oauth, name='oauth'),
    # path('profile/', include('users.urls')),
    # path('signup/', users_views.signup, name='signup'),
    # path('logout/', users_views.Logout, name='logout'),
]

# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# if settings.DEBUG == False:
#     handler404 = "home.views.errorPage404"
#     handler500 = "home.views.errorPage500"
