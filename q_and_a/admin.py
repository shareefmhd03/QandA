from django.contrib import admin
from .models import Answer, Notification, PointsTable, Question


admin.site.register(Answer)
admin.site.register(Question)
# admin.site.register(Tags)
admin.site.register(PointsTable)
admin.site.register(Notification)
