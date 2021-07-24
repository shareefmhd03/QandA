from .models import Profile
from accounts.models import Accounts
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Accounts)
def post_save_profile(sender, instance, created, **kwrgs):
    if created:
        Profile.objects.create(user = instance)