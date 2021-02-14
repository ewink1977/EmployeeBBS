from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from posts.models import BBSPosts
from events.models import storeEvent
# DEPARTMENT DICTIONARY IMPORT!
from bbs.departments import departments


@login_required
def bbsMainView(request):
    context = {
        'deptList': departments,
        'eventList': storeEvent.objects.order_by('-start_date'),
    }
    return render(request, 'bbs/main.html', context)
