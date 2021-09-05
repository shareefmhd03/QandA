

# from q_and_a.models import PointsTable, Question
from .models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import Accounts
from allauth.account.signals import user_logged_in


@receiver(post_save, sender=Accounts)
def post_save_profile(sender, instance, created, **kwrgs):
    if created:
        print('new profile created')
        Profile.objects.create(user = instance)


@receiver(user_logged_in, sender=Accounts)
def user_logged_in(request, user,**kwargs):
    if user:
        print('new social created')
        if Profile.objects.filter(user = user).exists():
            print('user already exist')
        else:
            Profile.objects.create(user = user)
    

# @receiver(post_save, sender=)
# def post_save_profile_social(sender, instance, created, **kwrgs):
#     if created:
#         Profile.objects.create(user = instance)


# @receiver(post_save, sender = Question)
# def create_question_relation(sender, instance, created, **kwargs):
         
#     sender_ = instance.user.profile.asked_questions
#     receiver_ = instance.receiver

#     if created:
#         sender_.asked_questions.add(receiver_.question)
#         sender_.save()
