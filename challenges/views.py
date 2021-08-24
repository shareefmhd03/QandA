from django.shortcuts import redirect, render
from .models import ChallengeQuestion, ChallengeTopic, Solved, SolvedQuestions, SolvedQuestions

from django.shortcuts import render,HttpResponse
from django.conf import settings
import json
import requests


from django.contrib.auth.decorators import login_required
from profiles.models import Profile

def leaderboard(request):
    rankings = Solved.objects.all().order_by('-points')
    context ={
        'rankings':rankings,
    }
    return render(request, 'user/leaderboard.html',context)

def view_challenges(request):
    if request.user.is_authenticated:

        topics = ChallengeTopic.objects.all()

        context = {
        'topics':topics, 
        }
        return render(request,'user/view_challenges.html',context)
    else:
        return redirect('login_view')

API_ENDPOINT = "https://api.jdoodle.com/v1/execute"
 
client_id = "d62ccddd41da5d617c4e9c45d317f19f"
client_secret = "67297e3c6ff2e669f3d6549ffa59964311f980ae4740a5b7726fb5ae560ea087"

LANG_CODE = { 'c': 1, 'java': 3, 'cpp14': 3, 'python3': 3,'go': 3,
            'sql': 3,'csharp': 3,'dart': 3,'nodejs': 3,'kotlin': 2,'brainfuck': 0,}



def code_editor(request,topic):
    print(topic)
    if request.user.is_authenticated:
       
        quest = ChallengeQuestion.objects.get(id = topic)
        # solvedquestion = Solved.objects.filter(user = request.user, sol = True)
        context = {
            'question' : quest,
        }
        return render(request,'user/compiler/code_editor.html',context)
    else:
        return redirect('login_view')

def challenge_quest(request,topic):
    # solved = False
    # context = {}
    # li = []

    # quest = ChallengeQuestion.objects.filter(topic_id = topic)
    # quest = ChallengeQuestion.objects.filter(topic_id = topic)
    solved = Solved.objects.filter(questions__topic_id = topic).order_by('updated_at')

            
    context = {
        # 'question' : quest,/
        'solved' : solved,
    }
    return render(request, 'user/challenge_quest.html',context)


# @login_required(login_url='/accounts/login/')
def result(request,pk):
    if request.user.is_authenticated:
        if request.method == "POST":
            source = request.POST.get("script")
            lang = request.POST.get("lang")
            stdin = request.POST.get("stdin")
            u_id = request.user.id
            test = ChallengeQuestion.objects.get(id = pk)

            usr = Profile.objects.get(user_id=u_id)
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
            solved  = SolvedQuestions.objects.filter(user_id = request.user.id).exists()
            if solved:
                    user = SolvedQuestions.objects.get(user_id = request.user.id)
            else:
                    user = SolvedQuestions.objects.create(user_id = request.user.id,topic_id = test.topic.id)

            try:
                headers = {'Content-type': 'application/json'}
                r = requests.post(url = API_ENDPOINT, data = json.dumps(data), headers = headers)
                
                json_data = r.json()
                status = r.status_code
                output = json_data['output']

                if output:
                    output = output.replace("\n","")
                    
                if test.test_case1_sol == output:
                    user.challenges.add(test)  

                    if test in user.challenges.all():
                        solu = Solved.objects.filter(user = request.user, questions = test).exists()
                        if solu:
                            solu.sol = True
                            solu.points + 5
                            solu.save()          
                        else:
                            solv  = Solved.objects.create(user = request.user, questions = test, sol = True)
                            solv.save()
            except Exception as e:
                print(e)
                output = e
                            
            return HttpResponse(json.dumps({'output': json_data['output']}), content_type="application/json")
        else:
            return render(request,'user/compiler/code_editor.html',locals())
    else:
        return redirect('login_view')


def check_lang(self,lang):
    lang_array = self.lang.split(",")
    for lng in lang_array:
        if lng == lang:
            return False
    return True            

