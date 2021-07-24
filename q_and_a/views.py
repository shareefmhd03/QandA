from typing import Annotated
from q_and_a.models import Answer, Question
from django.contrib.auth import forms
from django.shortcuts import redirect, render
from .forms import AnswerForm, AskQusestionForm





def index(request):
    question = Question.objects.all()
    context = {
        'question':question,
    }
    return render(request, 'user/index.html', context)



# Create your views here.
def ask_question(request):
    print('in the view------------------')

    if request.method == 'POST':
        print('post working')
        form = AskQusestionForm(request.POST, request.FILES)
        if form.is_valid():
            print('valid form')
            title = form.cleaned_data['question_title']
            question = form.cleaned_data['question']
            attachment = form.cleaned_data['attachment']
            # tags = form.cleaned_data['tags'] 

            quest = Question(question_title = title, user = request.user, question= question, attachment=attachment)
            quest.save()
            return redirect('index')

    form = AskQusestionForm()
    context = {
        'form':form,
    }
    return render(request, 'user/ask_question.html',context)


def answer(request, question):
    if request.user.is_authenticated:
        quest = Question.objects.get(id = int(question))
        if request.method =='POST':
            print('post working')
            form = AnswerForm(request.POST, request.FILES)
            if form.is_valid():
                print('valid form')
                title = form.cleaned_data['answer_title']
                desc = form.cleaned_data['description']
                attach = form.cleaned_data['attachment']

                ans = Answer(answer_title = title, user = request.user, description = desc, attachment = attach, question = quest )
                ans.save()
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
   