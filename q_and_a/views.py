from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
# from django.views.decorators.http import require_GET, require_POST
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET
from django.http.response import HttpResponse
from django.db.models.aggregates import Count
from blog.models import Blog
from django.http.response import HttpResponse, JsonResponse
from q_and_a.models import Answer, Notification, PointsTable, Question
from profiles.models import Profile
from django.shortcuts import redirect, render
from .forms import AnswerForm, AskQusestionForm
from django.db.models import Q
import datetime

from accounts.models import Accounts
# from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
# from webpush import send_user_notification
# from django.views.decorators.csrf import csrf_exempt

from django.conf import settings

import json


def get_time():
    return datetime.datetime.now()


def index(request):
    context = {}
  
    if request.user.is_authenticated:
        context['user'] = request.user

    profile = Profile.objects.all().order_by()[:5]
    try:
        prof = Profile.objects.get(user=request.user)
        context['prof'] = prof
    except:
        pass
    question = Question.objects.all().order_by('-created_at')

    blogs = Blog.objects.all()

    context = {
        'question': question,

        'profile': profile,
        'blogs': blogs,
        # 'vapid_key': vapid_key,
    }

    return render(request, 'user/index.html', context)


def question_from_index(request):
    if request.method == 'POST':
        title = request.POST['title']
        quest = Question(question_title=title, user=request.user)
        quest.save()
        return redirect('question_list')


def ask_question(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AskQusestionForm(request.POST, request.FILES)
            if form.is_valid():
                title = form.cleaned_data['question_title']
                question = form.cleaned_data['question']
                quest = Question(question_title=title,
                                 user=request.user, question=question)
                quest.save()
                points = PointsTable.objects.get(user=request.user)
                points.point += 1
                points.save()
                return redirect('question_list')

        form = AskQusestionForm()
        context = {
            'form': form,
        }
        return render(request, 'user/ask_question.html', context)
    else:
        return redirect('login_view')



def edit_question(request, question):
    quest = Question.objects.get(slug=question)
    form = AskQusestionForm(instance=quest)
    if Question.objects.filter(user=request.user, slug=question).exists():
        solved = Question.objects.filter(
            user=request.user, slug=question).exists()
        if request.method == 'POST':
            form = AskQusestionForm(
                request.POST, request.FILES, instance=quest)
            if form.is_valid():
                title = request.POST['question_title']
                questi = request.POST['question']
                quest.title = title
                quest.question = questi
                quest.save()
                return redirect('question_list')
    context = {
        'form': form,
        'solved': solved,
    }
    return render(request, 'user/ask_question.html', context)



def edit_answer(request, pk):
    ans = Answer.objects.get(id=pk)
    form = AnswerForm(instance=ans)
    question = Question.objects.get(id=ans.question_id)
    if Answer.objects.filter(id=pk, user=request.user).exists():
        owner = Answer.objects.filter(id=pk, user=request.user).exists()
    else:
        owner = False

    if request.method == 'POST':
        form = AnswerForm(request.POST, request.FILES, instance=ans)
        if form.is_valid():
            title = request.POST['description']
            ans.description = title
            ans.save()
            return redirect('view_answer', question.slug)
    context = {
        'form': form,
        'answer': ans,
        'owner': owner,
    }
    return render(request, 'user/edit_answer.html', context)



def answer(request, question):
    webpush_settings = getattr(settings, 'WEBPUSH_SETTINGS', {})
    vapid_key = webpush_settings.get('VAPID_PUBLIC_KEY')
    owner = False

    #edit answer
    if request.user.is_authenticated:
        quest = Question.objects.get(id=int(question))
        if Answer.objects.filter(question_id=quest.id, user=request.user).exists():
            owner = Answer.objects.filter(
                question_id=quest.id, user=request.user).exists()
            print('here top')
            print(owner)
            if request.method == 'POST':
                ans = Answer.objects.get(
                    question_id=quest.id, user=request.user)
                form = AnswerForm(request.POST, request.FILES, instance=ans)
                if form.is_valid():
                    desc = form.cleaned_data['description']
                    ans.save()
                    # call the push notification function

                    return redirect('view_answer', quest.slug)
        else:
                #Post answer
            if request.method == 'POST':
                form = AnswerForm(request.POST, request.FILES)
                if form.is_valid():
                    desc = form.cleaned_data['description']
                    ans = Answer(user=request.user,
                                 description=desc, question=quest)
                    ans.save()
                    Notification.objects.create(
                        from_user=request.user, to_user=ans.question.user, answered=ans)
                    print('about to call the send_push')
                    # data = {'head': '', 'body': quest.question_title +
                    #         'answered', 'id': quest.user_id}
                    # send_push(request, data)
                    return redirect('view_answer', quest.slug)
            form = AnswerForm()
    context = {

        'owner': owner,
        'vapid_key': vapid_key,
        'user': request.user,
    }
    return render(request, 'user/login.html', context)



def delete_answer(request, pk):
    ans = Answer.objects.get(id=pk)
    ans.delete()
    quest = Question.objects.get(id=ans.question_id)
    return redirect('view_answer', quest.slug)



def view_answer(request, pk):
    context = {}
    webpush_settings = getattr(settings, 'WEBPUSH_SETTINGS', {})
    vapid_key = webpush_settings.get('VAPID_PUBLIC_KEY')
    author = False
    quest = Question.objects.filter(slug=pk)
    questt = Question.objects.get(slug=pk)

    try:
        if Question.objects.filter(user=request.user, slug=pk).exists():
            author = Question.objects.filter(
                user=request.user, slug=pk).exists()
            context['author'] = author
    except:
        pass
    answer = Answer.objects.filter(question_id__slug=pk).order_by('created_at')
    # try:
    #     if Answer.objects.filter(user = request.user):
    #         owner = True
    #         context['owner'] = True
    # except:
    #     pass

    profile = Profile.objects.get(user=questt.user)
    # now = get_time()
    # print(now.minute, 'now ')
    # for i in quest:
    # posted = questt.created_at
    # print(posted)
    # views = view_count(request,pk)
    # print(views,'dddddddddddd')
    if request.user.is_authenticated:
        questt.view_count.add(request.user)
        # questt.save()

    # questt.save()
    # print(questt.view_count,'AFTER')
    # for i  in answer:
    #     print(i.upvote_count(),'ooooooooooooooooo')
    #     upvote_count = i.upvote.count()
    #     downvote_count = i.downvote.count()
    # vote_average = upvote_count-downvote_count
    form = AnswerForm()
    context = {
        # 'vote_average':vote_average,
        'question': quest,
        'answer': answer,
        'form': form,
        'vapid_key': vapid_key,
        'profile': profile,
        # 'owner'    :owner,
        'author': author,
        'user': request.user,
    }
    return render(request, 'user/single_question.html', context)



def solved(request):
    if request.method == 'POST':
        print('inside post')

        ans_id = request.POST['data']
        print(ans_id)

        ans = Answer.objects.get(id=ans_id)
        points = PointsTable.objects.get(user=ans.user)
        question = Question.objects.get(id=ans.question_id)
        if question.solved == False:
            question.solved = True
            points.point += 5
            points.save()
            question.save()
        elif ans.is_solution == False:
            ans.is_solution = True
            ans.save()
        quest = Question.objects.get(id=ans.question_id)
        return redirect('view_answer', quest.slug)



def question_list(request):
    question = Question.objects.all().order_by('-created_at')
    popular_questions = Question.objects.annotate(q_count=Count('upvote'))
    recently_answered = Question.objects.filter(
        solved=True).order_by('updated_at')
    not_answered = Question.objects.filter(solved=False).order_by('updated_at')

    context = {
        'question': question,
        'popular_questions': popular_questions,
        'recently_answered': recently_answered,
        'not_answered': not_answered,

    }
    return render(request, 'user/questions_list.html', context)


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']

        if keyword:
            question = Question.objects.order_by('-created_at').filter(
                Q(question__icontains=keyword) | Q(question_title__icontains=keyword))

        else:
            return render(request, 'user/question_list.html')
    context = {
        'question': question,
    }
    return render(request, 'user/questions_list.html', context)


def search_question(request):
    title = request.GET.get('title')

    question_list = []
    if title:
        questions = Question.objects.filter(
            question_title__icontains=title)[:2]
        for question in questions:
            question_list.append(question.question_title)

    return JsonResponse({'status': 200, 'data': question_list})


def search_filter(request):

    title = request.GET.get('search')

    if title:
        questions = Question.objects.filter(question_title__icontains=title)
        data = questions.values()

        return JsonResponse(list(data), safe=False)


def voting_up(request):


    if request.user.is_authenticated:
        if request.method == 'POST':
            ans_id = request.POST.get('data')

            ans = Answer.objects.get(id=ans_id)
            ans.upvote.add(request.user)
            ans.downvote.remove(request.user)
            ans.save()

        return JsonResponse({'total_vote': ans.vote_total(), 'answer_id': ans_id})
    return redirect('index')


def voting_down(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            ans_id = request.POST.get('data')
            ans = Answer.objects.get(id=ans_id)
            ans.upvote.remove(request.user)
            ans.downvote.add(request.user)
            a = ans.upvote_count()
            b = ans.downvote_count()
            ans.save()
            total_vote = a-b

            return JsonResponse({'total_vote': total_vote, 'answer_id': ans_id})
    return redirect('index')


def voting_up_question(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            ques_id = request.POST.get('data')
            ques = Question.objects.get(id=ques_id)
            ques.upvote.add(request.user)
            ques.downvote.remove(request.user)
            ques.save()

        return JsonResponse({'total_vote': ques.vote_total(), 'answer_id': ques_id})
    return redirect('index')


def voting_down_question(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            ques_id = request.POST.get('data')
            ques = Question.objects.get(id=ques_id)
            ques.upvote.remove(request.user)
            ques.downvote.add(request.user)
            ques.save()
            return JsonResponse({'total_vote': ques.vote_total(), 'answer_id': ques_id})
    return redirect('index')


def notification_delete(request, notification_pk, *args, **kwargs):
    notification = Notification.objects.get(pk=notification_pk)

    notification.user_has_seen = True
    notification.save()

    return HttpResponse('Success', content_type='text/plain')


def notification_delete_ajax(request):
    va = request.POST['data']
    notification = Notification.objects.get(id=va)
    notification.user_has_seen = True
    notification.save()
    count = Notification.objects.filter(
        to_user=request.user, user_has_seen=False).count()
    print(count)
    return JsonResponse({'data': count})


# @csrf_exempt
# def send_push(request,data):
#     try:
#         # body = request.body
#         # data = json.loads(body)
#         # print(data)

#         if 'head' not in data or 'body' not in data or 'id' not in data:
#             return JsonResponse(status=400, data={"message": "Invalid data format"})

#         user_id = data['id']
#         user = get_object_or_404(Accounts, id=user_id)
#         payload = {'head': data['head'], 'body': data['body']}
#         send_user_notification(user=user, payload=payload, ttl=1000)
#         return JsonResponse(status=200, data={"message": "Web push successful"})
#     except TypeError:
#         return JsonResponse(status=500, data={"message": "An error occurred"})


# @require_GET
# def home(request):
#     webpush_settings = getattr(settings, 'WEBPUSH_SETTINGS', {})
#     vapid_key = webpush_settings.get('VAPID_PUBLIC_KEY')
#     user = request.user
#     return render(request, 'home.html', {user: user, 'vapid_key': vapid_key})


# @require_POST
# @csrf_exempt
# def send_push(request,data):
#     try:
#         body = request.body
#         data = {'head': 'sss', 'body': 'asdf', 'id': '15'}
#         print(data)

#         if 'head' not in data or 'body' not in data or 'id' not in data:
#             return JsonResponse(status=400, data={"message": "Invalid data format"})

#         user_id = data['id']
#         user = get_object_or_404(Accounts, pk=user_id)

#         payload = {'head': data['head'], 'body': data['body']}

#         send_user_notification(user=user, payload=payload, ttl=1000)

#         return JsonResponse(status=200, data={"message": "Web push successful"})
#     except TypeError:
#         return JsonResponse(status=500, data={"message": "An error occurred"})
