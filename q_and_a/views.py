from typing import Annotated

from django.http.response import JsonResponse
from q_and_a.models import Answer, Question, Tags
from django.contrib.auth import forms
from django.shortcuts import redirect, render
from .forms import AnswerForm, AskQusestionForm


def index(request):
    question = Question.objects.all().order_by('-created_at')
    context = {
        'question':question,
    }
    return render(request, 'user/index.html', context)

def index_call(request):
    if request.is_ajax():
        print('ajax')
        question = Question.objects.all().last()
        print(question)
        return JsonResponse({
            'msg':'success',
        })
    return redirect('index')

def question_from_index(request):
    if request.method == 'POST':
        
        title = request.POST['title']
        quest = Question(question_title = title, user = request.user)
        quest.save()
        return JsonResponse({
            'msg':'success',
        })

def ask_question(request):
    try:
        if request.user.is_authenticated:
            if request.method == 'POST':
                form = AskQusestionForm(request.POST, request.FILES)
                if form.is_valid():

                    title = form.cleaned_data['question_title']
                    question = form.cleaned_data['question']

                    quest = Question(question_title = title, user = request.user, question= question)
                    quest.save()
                    return redirect('index')

            form = AskQusestionForm()
            context = {
                'form':form,
            }
            return render(request, 'user/ask_question.html',context)
        else:
            return redirect('login_view')
    except Exception as e:
        print(e)




def edit_question(request, question):
    
    quest = Question.objects.get(id = question)
    form = AskQusestionForm(instance=quest)
    if Question.objects.filter(user = request.user, id= question).exists():
        if request.method == 'POST':
            form = AskQusestionForm(request.POST, request.FILES, instance = quest)
            print('post request')
            if form.is_valid():
                print('valid')
                title = request.POST['question_title']
                questi = request.POST['question']
                quest.title = title
                quest.question = questi
                quest.save()
                return redirect('index')
    context = {
            'form':form,
            }
    return render(request, 'user/ask_question.html',context)
    


def answer(request, question):
    if request.user.is_authenticated:
        quest = Question.objects.get(id = int(question))
        if request.method =='POST':
            form = AnswerForm(request.POST, request.FILES)
            if form.is_valid():
                title = form.cleaned_data['answer_title']
                desc = form.cleaned_data['description']
                attach = form.cleaned_data['attachment']

                ans = Answer(answer_title = title, user = request.user, description = desc, attachment = attach, question = quest )
                ans.save()
                return redirect('view_answer', int(question))
        form = AnswerForm()
        context ={
            'form':form,
        }
        return render(request,'user/answer_form.html',context)
    return render(request, 'user/login.html')



def view_answer(request, pk):
    quest = Question.objects.filter(id = pk)
    answer = Answer.objects.filter(question_id = pk)
    context = {
        'question':quest,
        'answer':answer,
    }
    return render(request, 'user/single_question.html', context)

def related_questions(request):
    rl = Question.objects.filter(tag = tag)