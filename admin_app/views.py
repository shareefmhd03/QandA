from tutorials.forms import McQForm, TutorialForm
from tutorials.models import McqQuestions, Topics, Tutorial
from accounts.models import Accounts
from django.shortcuts import render,redirect
# from accounts.views import session_check
from accounts.forms import RegistrationForm

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