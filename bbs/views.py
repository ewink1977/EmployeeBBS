from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from posts.models import BBSPosts

# DEPARTMENT DICTIONARY
departments = {
    1: 'Front-Line Crew',
    2: 'Kitchen',
    3: 'Maintainance',
    4: 'Shift Management',
    5: 'Store Management',
    6: 'Reserved',
    7: 'Reserved',
    8: 'Storewide',
    9: 'Information Technology'
}


@login_required
def bbsMainView(request):
    context = {
        'deptList': departments,
    }
    return render(request, 'bbs/main.html', context)
