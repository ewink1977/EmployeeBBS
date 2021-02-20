from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from posts.models import BBSPosts
from events.models import storeEvent
from users.models import UserTimeManagement
from datetime import datetime
# DEPARTMENT DICTIONARY IMPORT!
from bbs.departments import departments


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
        eventFilter = storeEvent.objects.filter(department = 8 or request.user.userProfile.department, end_date__gte = now).order_by('start_date')
    stickyPosts = BBSPosts.objects.filter(priority = 2)
    storewidePosts = BBSPosts.objects.filter(department = 8)
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