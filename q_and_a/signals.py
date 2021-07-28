from django.db.models.signals import post_save
from .models import PointsTable
from accounts.models import Accounts
from django.dispatch import receiver



@receiver(post_save, sender= Accounts)
def create_points_table(sender, instance, created, **kwargs):
    if created:
        PointsTable.objects.create(user  = instance)


# def update_points_table(sender, instance, created, **kwargs):
#     if created == False:
#         instance.save()
