from django.urls import path
from .views import *
urlpatterns = [
    path('',index, name = 'index'),
    path('ask_question/', ask_question, name = 'ask_question'),
    path('view_answer/<int:pk>', view_answer, name = 'view_answer'),
    path('answer/<str:question>', answer, name = 'answer'),
    path('edit_question/<slug:question>', edit_question, name = 'edit_question'),
    path('question_from_index', question_from_index, name = 'question_from_index'),
    # path('index_call', index_call, name = 'index_call'),
    path('solved/', solved, name = 'solved'),
    path('question_list/', question_list, name = 'question_list'),
    path('search/', search, name = 'search'),
    path('search_question/', search_question, name = 'search'),
    path('search_filter/', search_filter, name = 'search_filter'),

]