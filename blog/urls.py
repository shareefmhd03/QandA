from django.urls import path
from .views import view_blog,add_blog

urlpatterns = [
    path('view_blog', view_blog, name='view_blog'),
    path('add_blog', add_blog, name='add_blog'),
]