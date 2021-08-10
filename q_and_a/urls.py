from django.urls import path
from .views import *
urlpatterns = [
    path('',index, name = 'index'),
    path('ask_question/', ask_question, name = 'ask_question'),
    path('view_answer/<slug:pk>', view_answer, name = 'view_answer'),
    path('answer/<str:question>', answer, name = 'answer'),
    path('edit_question/<slug:question>', edit_question, name = 'edit_question'),
    path('question_from_index', question_from_index, name = 'question_from_index'),
    path('solved/', solved, name = 'solved'),
    path('question_list/', question_list, name = 'question_list'),
    path('search/', search, name = 'search'),
    path('search_question/', search_question, name = 'search'),
    path('search_filter/', search_filter, name = 'search_filter'),
    path('voting_up/', voting_up, name = 'voting_up'),
    path('voting_down/', voting_down, name = 'voting_down'),
    path('voting_up_question/', voting_up_question, name = 'voting_up_question'),
    path('voting_down_question/', voting_down_question, name = 'voting_down_question'),

]