from django.shortcuts import render

from django.shortcuts import render,HttpResponse
from django.conf import settings
import json
import requests
import base64
from django.contrib.auth.decorators import login_required
from profiles.models import Profile, User_profile
# from user.models import User_profile

def view_challenges(request):
    return render(request,'user/view_challenges.html')

# def runcode(request):
#     print('hello')
#     if request.method == "POST":
#         codeareadata = request.POST['codearea']
#         try:
#             original_stdout = sys.stdout
#             sys.stdout = open('file.txt', 'w') 
#             exec(codeareadata)
#             sys.stdout.close()
#             sys.stdout = original_stdout  
#             output = open('file.txt', 'r').read()
#         except Exception as e:
#             sys.stdout = original_stdout
#             output = e
#         context = {
#             "code":codeareadata,
#             "output":output,
#             }
#         return render(request , 'user/view_challenges.html', context)




API_ENDPOINT = "https://api.jdoodle.com/v1/execute"

client_id = "d62ccddd41da5d617c4e9c45d317f19f"
client_secret = "67297e3c6ff2e669f3d6549ffa59964311f980ae4740a5b7726fb5ae560ea087"

LANG_CODE = { 'c': 1, 'java': 3, 'cpp14': 3, 'python3': 3,'go': 3,
            'sql': 3,'csharp': 3,'dart': 3,'nodejs': 3,'kotlin': 2,'brainfuck': 0,}


# @login_required(login_url='/accounts/login/')
def code_editor(request):
    return render(request,'user/compiler/code_editor.html')


# @login_required(login_url='/accounts/login/')
def result(request):
    print('inthe view')
    if request.method == "POST":
        print('inthe post')
        source = request.POST.get("script")
        lang = request.POST.get("lang")
        stdin = request.POST.get("stdin")
        u_id = request.user.id
        print(u_id,'---------')
        usr = User_profile.objects.get(user_id=u_id)
        usr.n_subm += 1
        if check_lang(usr,lang):
            usr.lang +=lang+","
        usr.save()
        data = {'clientId':client_id,
                'clientSecret':client_secret,
                'script':source,
                'stdin':stdin,
                'language':lang,
                'versionIndex':LANG_CODE[lang],
            }
             
        try:
            headers = {'Content-type': 'application/json'}
            r = requests.post(url = API_ENDPOINT, data = json.dumps(data), headers = headers)
            json_data = r.json()
            print(json_data)
            status = r.status_code
            print(status)
            #output = Robject(r.json())
            output = json_data['output']
            if not output:
                output = message.replace("\n","<br>")
        except Exception as e:
            print(e)
            output = settings.ERROR_MESSAGE
        print(output)   
        return HttpResponse(json.dumps({'output': json_data['output']}), content_type="application/json")
    else:
        return render(request,'user/compiler/code_editor.html',locals())


def check_lang(self,lang):
    lang_array = self.lang.split(",")
    for lng in lang_array:
        if lng == lang:
            return False
    return True            

