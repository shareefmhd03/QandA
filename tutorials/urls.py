
from tutorials.views import tutorials,single_tutorial,take_test
from django.urls import path

urlpatterns = [
    path('',tutorials, name='tutorials'),
    path('single_tutorial/<slug:slug>',single_tutorial, name='single_tutorial'),
    path('take_test/<int:id>',take_test, name='take_test'),
]