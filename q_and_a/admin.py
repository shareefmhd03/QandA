from django.contrib import admin
from django.db.models.query_utils import Q
from .models import Answer, Question


# admin.site.register(Tags)
admin.site.register(Answer)
admin.site.register(Question)
