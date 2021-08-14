from tutorials.models import Topics
from django.contrib.auth import authenticate
from django.http.response import JsonResponse
from accounts.models import Accounts
from django.shortcuts import redirect, render
from .forms import RegistrationForm
from django.contrib.auth import logout,login
from django.contrib import messages
from django.views.decorators.cache import cache_control
from django.contrib import messages 

# Create your views here.

# def session_check(request):
#     if request.session['loggedin'] == True:
#         return True
@cache_control(no_cache=True, must_revalidate=True, no_store=True)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
            if request.method == 'POST':
                usernam   = request.POST['username']
                passwd  = request.POST['password1']
                
                user = authenticate(request, username = usernam, password=passwd)

                login(request, user)
                return redirect('index')
    
                
            return render(request, 'user/login.html')


# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:

        form = RegistrationForm(request.POST or None)
        if request.method == 'POST':

            if form.is_valid():

                firstname = form.cleaned_data['first_name']
                lastname = form.cleaned_data['last_name']
                email = form.cleaned_data['email']
                phone = form.cleaned_data['phone']
                password1 = form.cleaned_data['password1']
                password2 = form.cleaned_data['password2']
                username = email.split('@')[0]+''
                user = Accounts.objects.create_user(
                    first_name = firstname, last_name = lastname, email = email, password=password1, phone = phone,username = username)
                user.save()
                # messages.success(request, 'Account created successfully')
                return redirect('login_view')
        # form = RegistrationForm()
        context = {
            'form': form,
        }
        return render(request, 'user/signup.html',context)




def logout_view(request):
    logout(request)
    return redirect ('login_view')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin_dashboard(request):
    try:
        if request.session['loggedin']:
       
            
            return render(request, 'admin/dashboard.html')
    except:
        return render(request, 'admin/loginPage.html')



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin_login(request):
    username = 'admin'
    password = '123'

    if request.method == 'POST':
        uname = request.POST['username']
        pswd = request.POST['password']

        if pswd == password and uname == username:
            request.session['loggedin'] = True
            return redirect('admin_dashboard')
        else:
            return redirect('admin_login')
    return render(request, 'admin/loginPage.html')

def admin_logout(request):
    del request.session['loggedin']
    return redirect('admin_login')


def validate_username(request):
    email = request.GET.get('username', None)
    print(email)
    data = {
        'is_taken': Accounts.objects.filter(username=email).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this email already exists.'
    return JsonResponse(data)
def validate_email(request):

    email = request.GET.get('email', None)
    print(email)
    data = {
        'is_taken': Accounts.objects.filter(email=email).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this email already exists.'
    return JsonResponse(data)
