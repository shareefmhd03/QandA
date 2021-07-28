from django.contrib import admin
from .models import Answer, PointsTable, Question, Tags


admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Tags)
admin.site.register(PointsTable)
