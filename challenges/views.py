from django.shortcuts import render
import sys

def view_challenges(request):

    return render(request,'user/view_challenges.html')

def runcode(request):
    print('hello')
    if request.method == "POST":
        codeareadata = request.POST['codearea']
        try:
            original_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w') 
            exec(codeareadata)
            sys.stdout.close()
            sys.stdout = original_stdout  
            output = open('file.txt', 'r').read()
        except Exception as e:
            sys.stdout = original_stdout
            output = e
        context = {
            "code":codeareadata,
            "output":output,
            }
        return render(request , 'user/view_challenges.html', context)
