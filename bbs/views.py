from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from posts.models import BBSPosts
# DEPARTMENT DICTIONARY IMPORT!
from bbs.departments import departments


@login_required
def bbsMainView(request):
    context = {
        'deptList': departments,
    }
    return render(request, 'bbs/main.html', context)
