# Generated by Django 3.2.5 on 2021-08-10 17:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('q_and_a', '0005_delete_sample'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='downvote',
            field=models.ManyToManyField(related_name='ques_dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='upvote',
            field=models.ManyToManyField(related_name='ques_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
