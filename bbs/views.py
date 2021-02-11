from django.shortcuts import render, HttpResponse
from posts.models import BBSPosts, BBSReply

def bbsMainView(request):
    # return HttpResponse('<h1>SUCCESS</h1>')
    return render(request, 'bbs/main.html')
