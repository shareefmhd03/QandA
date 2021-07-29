from django.shortcuts import render

# Create your views here.
def community_page(request):
    return render(request, 'user/community_page.html')