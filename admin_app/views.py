from accounts.models import Accounts
from django.shortcuts import render,redirect
# from accounts.views import session_check
from accounts.forms import RegistrationForm

# Create your views here.

def user_mgmt(request):
    if request.session['loggedin']:
        users = Accounts.objects.exclude(is_superuser =True)
        context = {
            'users':users,
        }
        for i in users:
            print(i.is_active)
        return render(request, 'admin/usermgmt.html',context)
    return render(request, 'admin/loginPage.html')

def add_user(request):
    
    if request.session['loggedin']:
        if request.method == "POST":
            form = RegistrationForm(request.POST)
            if form.is_valid():
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
    else:
        return render(request, 'admin/loginPage.html')
        

def user_unblock(request):
    user_id = request.POST['data']
    user = Accounts.objects.get(id = user_id)
    if user.is_active == True:
        user.is_active = False
    else:
        user.is_active = False

