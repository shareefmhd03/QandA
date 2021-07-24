from django.contrib import auth
from accounts.models import Accounts
from django.shortcuts import redirect, render
from . forms import RegistrationForm
from django.contrib.auth import logout

# Create your views here.

def session_check(request):
    if request.session['loggedin'] == True:
        return True

def login_view(request):

    if request.method == 'POST':
        usernam   = request.POST['username']
        password  = request.POST['password1']
        user = auth.authenticate(username = usernam, password=password)
        auth.login(request, user)
        return redirect('index')
    return render(request, 'user/login.html')



def register(request):
    if request.method == 'POST':

        form = RegistrationForm(request.POST)
        if form.is_valid():

            firstname = form.cleaned_data['first_name']
            lastname = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            print(firstname,lastname)
            username = email.split('@')[0]+''
            user = Accounts.objects.create_user(
                first_name = firstname, last_name = lastname, email = email, password=password1, phone = phone,username = username)
            user.save()
            return redirect('login_view')
    form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'user/login.html',context)

def index(request):
    return render(request, 'user/index.html')


def logout_view(request):
    logout(request)
    return redirect ('login_view')




def admin_dashboard(request):
    if request.session['loggedin']:
        return render(request, 'admin/dashboard.html')


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