from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from posts.models import BBSPosts
from events.models import storeEvent
from users.models import UserTimeManagement
from datetime import datetime
from itertools import chain
from bbs.departments import departments


def landing_page(request):
    return render(request, 'bbs/landing.html')

def error_404_view(request, exception):
    return render(request, 'bbs/404.html')

def documentation(request):
    return render(request, 'bbs/documentation.html')

@login_required
def bbsMainView(request):
    now = datetime.now()
    if request.user.userProfile.department >= 6:
        # 6+ ARE MANAGERS, SO THEY GET ALL POSTS AND EVENTS.
        postFilter = BBSPosts.objects.filter(priority = 1, is_reply = False)
        eventFilter = storeEvent.objects.filter(end_date__gte = now).order_by('start_date')
    else:
        # <6 ARE NORMAL STAFF, SO THEY ONLY SEE WHAT THEY NEED TO SEE!
        postFilter = BBSPosts.objects.filter(priority = 1, department = request.user.userProfile.department, is_reply = False)
        eventFilterDept = storeEvent.objects.filter(department = request.user.userProfile.department, end_date__gte = now).order_by('start_date')
        eventFilterStorewide = storeEvent.objects.filter(department = 8, end_date__gte = now).order_by('start_date')
        eventFilter = sorted(chain(eventFilterDept, eventFilterStorewide), key=lambda data: data.start_date)
    stickyPosts = BBSPosts.objects.filter(
        priority=2, department=request.user.userProfile.department, is_reply=False)
    storewidePosts = BBSPosts.objects.filter(department=8, is_reply=False)
    paginator = Paginator(postFilter.order_by('-created_at'), 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # GET THE USER'S LAST PUNCH.
    lastPunch = UserTimeManagement.objects.filter(user = request.user).last()
    # GOTTA MAKE THIS WORK FOR PEOPLE WHO HAVE NEVER CLOCKED IN BEFORE AND HAVE NO TIME RECORDS!
    if lastPunch:
        lastPunchBoolean = lastPunch.clocked_in
    else:
        lastPunchBoolean = False

    context = {
        'deptList': departments,
        'eventList': eventFilter,
        'page_obj': page_obj,
        'storewidePosts': storewidePosts,
        'stickyPosts': stickyPosts,
        'timeBoolean': lastPunchBoolean,
    }
    return render(request, 'bbs/main.html', context)
