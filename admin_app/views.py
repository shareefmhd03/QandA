from django.db.models.aggregates import Count
from q_and_a.models import Answer, Question
from challenges.models import ChallengeQuestion
from challenges.forms import ChallengeTopicForm, challengeForm
from tutorials.forms import McQForm, TutorialForm
from tutorials.models import McqQuestions, Topics, Tutorial
from accounts.models import Accounts
from django.shortcuts import render,redirect
# from accounts.views import session_check
from datetime import timezone
from datetime import datetime,timedelta

from accounts.forms import RegistrationForm
from django.views.decorators.cache import cache_control

# Create your views here.

def user_mgmt(request):
    try:
        if request.session['loggedin']:
            users = Accounts.objects.exclude(is_superuser =True).order_by('id')
            
            context = {
                'users':users,  
            }
            return render(request, 'admin/usermgmt.html',context)
    except:
        return render(request, 'admin/loginPage.html')

def add_user(request):
    try:
        if request.session['loggedin']:
            if request.method == "POST":
                form = RegistrationForm(request.POST)
                if form.is_valid():
                    print('valid')
                    firstname = form.cleaned_data['first_name']
                    lastname = form.cleaned_data['last_name']
                    email = form.cleaned_data['email']
                    phone = form.cleaned_data['phone']
                    password1 = form.cleaned_data['password1']
                    # password2 = form.cleaned_data['password2']
                    username = email.split('@')[0]+''
                    user = Accounts.objects.create_user(
                        first_name = firstname, last_name = lastname, email = email, password=password1, phone = phone,username = username)
                    user.save()
                    return redirect('user_mgmt')

            else:
                form = RegistrationForm()
                return render(request, 'admin/add_user.html')
   
    except:
        return render(request, 'admin/loginPage.html')
        

def user_unblock(request):
    try:
        if request.method == "POST":
            user_id = request.POST['data']
            user = Accounts.objects.get(id = user_id)
            if user.is_active == True:
                user.is_active = False
                user.save()
                print(user.is_active)

            elif user.is_active == False :
                user.is_active = True
                user.save()
        return redirect('user_mgmt')
    except:
        return render(request, 'admin/loginPage.html')



def delete_user(request):
    try:
        if request.method == "POST":
            user_id = request.POST['data']
            user = Accounts.objects.get(id = user_id)
            user.delete()

        return redirect('user_mgmt')
    except:
        return render(request, 'admin/loginPage.html')


def view_tutorials(request):
    try:

        if request.session['loggedin']:
            tutorials = Tutorial.objects.all()
            context ={
                'tutorials':tutorials,
            }
            return render(request, 'admin/tutorials.html',context)
        
    except:
        return render(request, 'admin/loginPage.html')

def add_tutorials(request):

    try:
        if request.method == 'POST':
            form = TutorialForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('view_tutorials')

        form = TutorialForm()
        context={
            'form':form,
        }
        return render(request, 'admin/add_tutorials.html',context)
    except:
        return render(request, 'admin/loginPage.html')

def view_tutorial(request,id):
    try:
        if request.session['loggedin']:
            tutorials = Tutorial.objects.get(id = id)
            context ={
                'tutorials':tutorials,
            }
            return render(request, 'admin/view_tutorial.html',context)
    
    except:
        return render(request, 'admin/loginPage.html')


def add_mcq(request):
    try:
        if request.session['loggedin']:
            if request.method == 'POST':
                form = McQForm(request.POST, request.FILES)
                if form.is_valid():
                    form.save()
                    return redirect('view_tutorials')

            form = McQForm()
            context={
                'form':form,
            }
            return render(request, 'admin/addmcq.html',context)
    except:
        return render(request, 'admin/loginPage.html')

def mcqquestions(request,id):
    try:
        if request.session['loggedin']:
            mcq = McqQuestions.objects.filter(topic_id =id)
            
            context={
                'mcqs':mcq,
            }
            return render(request, 'admin/mcqquestions.html',context)
    except:
        return render(request, 'admin/loginPage.html')


def all_topics(request):
    try:
        if request.session['loggedin']:
            topics = Topics.objects.all()
            context ={
                'topics':topics
            }
            return render(request, 'admin/all_topics.html',context)
    except:
        return render(request, 'admin/loginPage.html')

def edit_tutorials(request,id):
    try:
        if request.session['loggedin']:
            tutorials = Tutorial.objects.get(id = id)
            form = TutorialForm(instance = tutorials)
            if request.method == 'POST':
                    form = TutorialForm(request.POST, request.FILES, instance = tutorials)
                    if form.is_valid():
                        titl = request.POST['title']
                        Abou = request.POST['About']
                        Imag = request.FILES['Image']
                        descriptio = request.POST['description']
                        tutoria = request.POST['tutorials']
                        tutorials.title=titl
                        tutorials.About=Abou
                        tutorials.Image = Imag
                        tutorials.description=descriptio
                        tutorials.tutorial=tutoria
                        tutorials.save()
                        return redirect('view_tutorials')

            context ={
                'form':form,
            }
            return render(request,'admin/add_tutorials.html',context)
    except:
        return render(request, 'admin/loginPage.html')



def view_challenges_admin(request):
        if request.session['loggedin']:
            print('itsloggedin')
            challenges = ChallengeQuestion.objects.all()
            context ={
                'challenges':challenges,
            }
            return render(request, 'admin/view_challenges.html',context)
    
        else:
            return render(request, 'admin/loginPage.html')

def add_challenges(request):
    form = challengeForm()
    if request.session['loggedin']:
        if request.method == 'POST':
                print('in post')
                form = challengeForm(request.POST, request.FILES)
                if form.is_valid():
                    print('valid')

                    print('formnot  Saved')
                    form.save()
                    print('formSaved')
                    return redirect('view_challenges_admin')

        
        context={
            'form':form,
        }
        return render(request, 'admin/add_challenges.html',context)
    else:
        print('login not available')
        return render(request, 'admin/loginPage.html')


def add_challenge_topic(request):
    try:
        if request.method == 'POST':
            form = ChallengeTopicForm(request.POST, request.FILES)
            if form.is_valid():
                
                form.save()
                return redirect('view_challenges_admin')

        form = ChallengeTopicForm()
        context={
            'form':form,
        }
        return render(request, 'admin/add_challenge_topic.html',context)
    except:
        return render(request, 'admin/loginPage.html')

def show_challenge(request,id):
    if request.session['loggedin']:
        challenge = ChallengeQuestion.objects.get(id = id)
        context ={
            'challenge':challenge,
        }
        return render(request, 'admin/show_challenge.html',context)

    else:
        return render(request, 'admin/loginPage.html')


def edit_challenge(request,id):

    if request.session['loggedin']:
        challenge = ChallengeQuestion.objects.get(id = id)
        form = challengeForm(instance = challenge)
        if request.method == 'POST':
                form = challengeForm(request.POST, request.FILES, instance = challenge)
                if form.is_valid():

                    titl = request.POST['title']
                    des = request.POST['desc']
                    challenge_quest = request.POST['challenge_question']
                    sample_inp = request.POST['sample_input']
                    sample_out = request.POST['sample_output']
                    test_case = request.POST['test_case1']
                    test_case_sol = request.POST['test_case1_sol']
 
                    challenge.title=titl

                    challenge.desc=des
                    challenge.challenge_question=challenge_quest
                    challenge.sample_input=sample_inp
                    challenge.sample_output=sample_out
                    challenge.test_case1=test_case
                    challenge.test_case1_sol=test_case_sol
                    challenge.save()
                    return redirect('view_challenges_admin')

        context ={
            'form':form,
        }
        return render(request,'admin/add_challenges.html',context)
    else:
        return render(request, 'admin/loginPage.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin_dashboard(request):
    today = datetime.now().date()
    tomorrow = datetime.now() + timedelta(days=1)
    yesterday = datetime.now() + timedelta(days=-1)

    if request.session['loggedin']:
            today_question_count = Question.objects.filter(created_at__gte = yesterday,created_at__lte = tomorrow ).count()
            today_questions = Question.objects.filter(created_at__gte = yesterday,created_at__lte = tomorrow )[:5]
            today_answer_count = Answer.objects.filter(created_at__gte = yesterday,created_at__lte = tomorrow ).count()
            today_user_count = Accounts.objects.all().count()
            today_challenge_count = ChallengeQuestion.objects.all().count()
            context = {
                'question_count':today_question_count,
                'answer_count':today_answer_count,
                'user_count':today_user_count,
                'challenge_count':today_challenge_count,
                'today':today,
                'today_questions':today_questions,
            }
             
            return render(request, 'admin/dashboard.html',context)

    return render(request, 'admin/loginPage.html')