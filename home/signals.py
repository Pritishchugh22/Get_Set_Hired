from django.dispatch import receiver
from allauth.account.signals import user_logged_in
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .models import UserProfile, CompanyProfile
import requests

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        CompanyProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
    instance.companyprofile.save()

@receiver(user_logged_in)
def profile_filler(request, **kwargs):
    user = request.user
    user.userprofile.isUser = True
    user.userprofile.save()

    provider = kwargs.get('sociallogin').__dict__.get('account').__dict__.get('provider')
    if provider == "linkedin_oauth2" and user.userprofile.image == "":
        print("filling_profile")
        access_token = kwargs.get('sociallogin').__dict__.get('token').__dict__.get('token')
        LI_PROFILE_API_ENDPOINT = 'https://api.linkedin.com/v2/me?projection=(id,profilePicture(displayImage~:playableStreams))'
        r = requests.get(LI_PROFILE_API_ENDPOINT, headers={
                        'Authorization': 'Bearer ' + access_token})
        image_url = r.json()['profilePicture']['displayImage~']['elements'][0]['identifiers'][0]['identifier']
        print(image_url)

        user.userprofile.image = image_url
        user.userprofile.save()