from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField
from django.db.models.fields.files import ImageField
from accounts.models import Accounts

# Create your models here.



class Posts(models.Model):
    image = models.ImageField(blank = True, upload_to = 'images')
    description = models.TextField()
    # author = models.ForeignKey(Accounts,on_delete=models.CASCADE)
    upvote = models.ManyToManyField(Accounts, default=None, blank = True)
    # downvote = models.ManyToManyField(Accounts, default=None)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.pk)

    def upvotedd_users(self):
        return self.upvote.all()

    def downvoted_users(self):
        return self.downvote.all()

    def upvote_count(self):
        return self.upvote.all().count()

    def downvote_count(self):
        return self.downvote.all().count()

    