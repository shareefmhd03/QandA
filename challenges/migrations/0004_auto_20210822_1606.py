# Generated by Django 3.2.5 on 2021-08-22 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('challenges', '0003_remove_challengequestion_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solvedquestion',
            name='challenges',
            field=models.ManyToManyField(related_name='solved_challenge', to='challenges.ChallengeQuestion'),
        ),
        migrations.CreateModel(
            name='SolvedQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challenges', models.ManyToManyField(related_name='solved_challenges', to='challenges.ChallengeQuestion')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='challenges.challengetopic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
