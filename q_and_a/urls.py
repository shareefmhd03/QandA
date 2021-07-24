from django.urls import path
from .views import ask_question,answer,view_answer,index

urlpatterns = [
    path('index/',index, name = 'index'),
    path('ask_question/', ask_question, name = 'ask_question'),
    path('view_answer/<int:pk>', view_answer, name = 'view_answer'),
    path('answer/<str:question>', answer, name = 'answer'),
]