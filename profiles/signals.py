

from q_and_a.models import PointsTable, Question
from .models import Profile
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from accounts.models import Accounts

@receiver(post_save, sender=Accounts)
def post_save_profile(sender, instance, created, **kwrgs):
    if created:
        Profile.objects.create(user = instance)


# @receiver(post_save, sender = Question)
# def create_question_relation(sender, instance, created, **kwargs):
         
#     sender_ = instance.user.profile.asked_questions
#     receiver_ = instance.receiver

#     if created:
#         sender_.asked_questions.add(receiver_.question)
#         sender_.save()
