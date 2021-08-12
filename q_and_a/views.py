from django.db.models.aggregates import Count
from blog.models import Blog
from django.http.response import JsonResponse
from q_and_a.models import Answer, PointsTable, Question, Tags
from profiles.models import Profile

from django.shortcuts import redirect, render
from .forms import AnswerForm, AskQusestionForm
from django.db.models import Q
import datetime
from accounts.models import Accounts


def get_time():
    return datetime.datetime.now()


def index(request):
    profile = Profile.objects.all()
    question = Question.objects.all().order_by('-created_at')
    
    
    
    # popular_questions = Question.objects.filter
    
    blogs = Blog.objects.all()
    context = {
        'question':question,
        
        'profile':profile,
        'blogs':blogs,
    }
    return render(request, 'user/index.html', context)

def question_from_index(request):
    if request.method == 'POST':
        title = request.POST['title']
        quest = Question(question_title = title, user = request.user)
        quest.save()
        return redirect('index')

def ask_question(request):
    try:
        
        if request.user.is_authenticated:

            if request.method == 'POST':

                form = AskQusestionForm(request.POST, request.FILES)
                if form.is_valid():
                    title    = form.cleaned_data['question_title']
                    question = form.cleaned_data['question']
                    
                    quest = Question(question_title = title, user = request.user, question= question)
                    quest.save()
                    points = PointsTable.objects.get(user = request.user)

                    points.point+=1

                    points.save()
                    return redirect('question_list')

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
    quest = Question.objects.get(slug = question)
    form = AskQusestionForm(instance=quest)
    if Question.objects.filter(user = request.user, slug= question).exists():
        solved = Question.objects.filter(user = request.user, slug= question).exists()
        if request.method == 'POST':
            form = AskQusestionForm(request.POST, request.FILES, instance = quest)
            if form.is_valid():
                title = request.POST['question_title']
                questi = request.POST['question']
                quest.title = title
                quest.question = questi
                quest.save()
                return redirect('index')
    context = {
            'form':form,
            'solved':solved,
            }
    return render(request, 'user/ask_question.html',context)
    


def answer(request, question):
    if request.user.is_authenticated:
        quest = Question.objects.get(id = int(question))
        if Answer.objects.filter(question_id = quest.id,user = request.user).exists():
            print('here top')
            if request.method =='POST':
                ans =  Answer.objects.get(question_id =quest.id ,user = request.user)
                form = AnswerForm(request.POST, request.FILES, instance=ans)
                if form.is_valid():
                    # title = form.cleaned_data['answer_title']
                    desc = form.cleaned_data['description']
                    
                    ans.save()
                    return redirect('view_answer', quest.slug)
        else:
            print('here bottom')
            if request.method =='POST':
                form = AnswerForm(request.POST, request.FILES)
                if form.is_valid():
                    # title = form.cleaned_data['answer_title']
                    desc = form.cleaned_data['description']
                    ans = Answer(user = request.user, description = desc, question = quest )
                    ans.save()
                    return redirect('view_answer', quest.slug)
        form = AnswerForm()
        context ={
            'form':form,
        }
    return render(request, 'user/login.html')



def view_answer(request, pk):
    
    quest = Question.objects.filter(slug = pk)
    questt = Question.objects.get(slug = pk)
    author = Question.objects.filter(user = request.user, slug= pk).exists()
    answer = Answer.objects.filter(question_id__slug = pk).order_by('created_at')
    profile = Profile.objects.get(user = questt.user)
    now = get_time()
    print(now.minute, 'now ')
    # for i in quest:
    posted = questt.created_at
    # print(posted)
    
    # for i  in answer:
    #     print(i.upvote_count(),'ooooooooooooooooo')
    #     upvote_count = i.upvote.count()
    #     downvote_count = i.downvote.count()
    # vote_average = upvote_count-downvote_count
    form = AnswerForm()
    context = {
        # 'vote_average':vote_average,
        'question':quest,
        'answer':answer,
        'author':author,
        'form':form,
        'profile':profile,
    }
    return render(request, 'user/single_question.html', context)



def solved(request):
    if request.method == 'POST':
        print('inside post')
        
        ans_id = request.POST['data']
        print(ans_id)
        
        ans = Answer.objects.get(id =ans_id)
        points = PointsTable.objects.get(user = ans.user)
        question = Question.objects.get(id  = ans.question_id)
        if question.solved == False:
            question.solved = True
            points.point+=5
            points.save()
            question.save()
        
        elif ans.is_solution == False:
                ans.is_solution = True
                ans.save()
        quest = Question.objects.get(id  = ans.question_id)
        return redirect('view_answer',quest.slug)



def question_list(request):
    question = Question.objects.all().order_by('-created_at')
    popular_questions = Question.objects.annotate(q_count=Count('upvote'))
    recently_answered = Question.objects.filter(solved=True).order_by('updated_at')
    not_answered = Question.objects.filter(solved=False).order_by('updated_at')

    context={
        'question':question,
        'popular_questions':popular_questions,
        'recently_answered':recently_answered,
        'not_answered':not_answered,
    }
    return render(request, 'user/questions_list.html', context)



def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']

        if keyword:
            question = Question.objects.order_by('-created_at').filter(
                Q(question__icontains=keyword) | Q(question_title__icontains=keyword))

        else:
            return render(request, 'user/index.html')
    context = {
        'question': question,
    
    }
    return render(request, 'user/questions_list.html', context)



def search_question(request):
    title = request.GET.get('title')
    print(title)
    question_list =[]
    if title:
        questions = Question.objects.filter(question_title__icontains = title)[:2]
        for question in questions:
            question_list.append(question.question_title)

    return JsonResponse({'status':200, 'data': question_list})


def search_filter(request):
    
    title = request.GET.get('search')
    print(title)
    if title:
        
        questions = Question.objects.filter(question_title__icontains = title)
        data=questions.values()
        print(data)
        return JsonResponse(list(data),safe=False)
        # return JsonResponse({'status':200, 'data': questions})
    # question = Question.objects.all().order_by('-created_at')
    # context = {
    #     'question': question,
    
    # }
    # return render(request, 'user/test.html',context)


def voting_up(request):
    # points = PointsTable.objects.get

    if request.user.is_authenticated:
        if request.method =='POST':
            ans_id = request.POST.get('data')
            print(ans_id,'yyyy')
            ans = Answer.objects.get(id = ans_id)
            a = ans.upvote_count()
            b = ans.downvote_count()
            ans.upvote.add(request.user)
            ans.downvote.remove(request.user)
            ans.save()
            # total_vote = a-b

        return JsonResponse({'total_vote':ans.vote_total(),'answer_id':ans_id})
    return redirect('index')


def voting_down(request):
    # points = PointsTable.objects.get
    if request.user.is_authenticated:
        if request.method =='POST':
            ans_id = request.POST.get('data')
            ans = Answer.objects.get(id = ans_id)
            ans.upvote.remove(request.user)
            ans.downvote.add(request.user)
            a = ans.upvote_count()
            b = ans.downvote_count()
            ans.save()
            total_vote = a-b
            # ans.downvote.clear()
            return JsonResponse({'total_vote':total_vote,'answer_id':ans_id})
    return redirect('index')


# def popular_questions(request):
    

#     return render(request, 'user/question_list.html')



def voting_up_question(request):
    # points = PointsTable.objects.get
    print('hi')
    if request.user.is_authenticated:
        if request.method =='POST':
            ques_id = request.POST.get('data')
            ques = Question.objects.get(id = ques_id)
            ques.upvote.add(request.user)
            ques.downvote.remove(request.user)
            ques.save()


        return JsonResponse({'total_vote':ques.vote_total(),'answer_id':ques_id})
    return redirect('index')

def voting_down_question(request):
    if request.user.is_authenticated:
        if request.method =='POST':
            ques_id = request.POST.get('data')
            ques = Question.objects.get(id = ques_id)
            ques.upvote.remove(request.user)
            ques.downvote.add(request.user)
            ques.save()
            return JsonResponse({'total_vote':ques.vote_total(),'answer_id':ques_id})
    return redirect('index')