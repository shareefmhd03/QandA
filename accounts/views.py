from tutorials.models import Topics
from django.contrib.auth import authenticate
from django.http.response import HttpResponse, JsonResponse
from accounts.models import Accounts
from django.shortcuts import redirect, render
from .forms import RegistrationForm
from django.contrib.auth import logout, login
from django.contrib import messages
from django.views.decorators.cache import cache_control
from django.contrib import messages
import random
from twilio.rest import Client
from decouple import config


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            usernam = request.POST['username']
            passwd = request.POST['password1']

            try:
                user = authenticate(request, username=usernam, password=passwd)
                use = Accounts.objects.get(username=usernam)
                if use.is_active == False:
                    return redirect('otp_login')

                login(request, user)
                return redirect('question_list')
            except:
                messages.error(request, 'Invalid username or Password')
                return render(request, 'user/login.html')

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
                    first_name=firstname, last_name=lastname, email=email, password=password1, phone=phone, username=username, is_active=False)
                user.save()
                # messages.success(request, 'Account created successfully')
                return redirect('otp_login')
        # form = RegistrationForm()
        context = {
            'form': form,
        }
        return render(request, 'user/signup.html', context)


def logout_view(request):
    logout(request)
    return redirect('index')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin_login(request):
    username = 'admin'
    password = '123'

    if request.method == 'POST':
        uname = request.POST['username']
        pswd = request.POST['password']
        print(uname)
        print(pswd)

        if pswd == password and uname == username:
            request.session['loggedin'] = True
            print(request.session['loggedin'])
            return redirect('admin_dashboard')
        else:

            return redirect('admin_login')
    else:
        return render(request, 'admin/loginPage.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin_logout(request):
    del request.session['loggedin']
    return redirect('admin_login')


def validate_username(request):
    email = request.GET.get('username', None)

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


def otp_login(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        otp = random.randint(100000, 999999)
        strotp = str(otp)
        account_sid = config('account_sid')
        auth_token = config('auth_token')

        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
                body="Your login OTP is"+strotp,
                from_='+13012816882',
                to='+91'+phone
            )
        request.session['otp'] = otp
        request.session['phone'] = phone
        messages.success(request, "OTP Sended Successfully")
        return redirect('verify_otp')
    return render(request, 'user/otplogin.html')


def verify_otp(request):
    if request.method == 'POST':
        enter_otp = request.POST['otp']
        otp = int(enter_otp)
        if request.session.has_key('otp'):
            sended_otp = request.session['otp']
            email = request.POST['email']

            if sended_otp == otp:
                print("in if")
                phone = request.session['phone']
                use = Accounts.objects.get(email=email)
                use.is_active = True
                del request.session['otp']
                del request.session['phone']
                use.save()
                return redirect('login_view')
            else:
                messages.error(request, "entered OTP is wrong")
                return redirect('otp_login')
        else:
            return redirect('otp_login')
    return render(request, 'user/verifyotp.html')


def social_login(requsest):
    return HttpResponse('dasfsdfadsf')