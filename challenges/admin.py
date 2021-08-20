from challenges.models import ChallengeQuestion, ChallengeTopic, SolvedQuestion
from django.contrib import admin

# Register your models here.
# admin.site.register(Challenge)
admin.site.register(ChallengeTopic)
admin.site.register(ChallengeQuestion)
admin.site.register(SolvedQuestion)