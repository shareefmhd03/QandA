from django.urls import path
from .views import ask_question,answer,view_answer,index,edit_question,question_from_index,index_call,solved,question_list,search

urlpatterns = [
    path('',index, name = 'index'),
    path('ask_question/', ask_question, name = 'ask_question'),
    path('view_answer/<int:pk>', view_answer, name = 'view_answer'),
    path('answer/<str:question>', answer, name = 'answer'),
    path('edit_question/<int:question>', edit_question, name = 'edit_question'),
    path('question_from_index', question_from_index, name = 'question_from_index'),
    # path('index_call', index_call, name = 'index_call'),
    path('solved/', solved, name = 'solved'),
    path('question_list/', question_list, name = 'question_list'),
    path('search/', search, name = 'search'),
]