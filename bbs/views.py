from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from posts.models import BBSPosts

@login_required
def bbsMainView(request):
    user = request.user
    return render(request, 'bbs/main.html')
