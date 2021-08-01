
from tutorials.views import tutorials,single_tutorial
from django.urls import path

urlpatterns = [
    path('',tutorials, name='tutorials'),
    path('single_tutorial/<slug:slug>',single_tutorial, name='single_tutorial'),
]