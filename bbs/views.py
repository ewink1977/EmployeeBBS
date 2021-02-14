from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from posts.models import BBSPosts
from events.models import storeEvent
# DEPARTMENT DICTIONARY IMPORT!
from bbs.departments import departments


@login_required
def bbsMainView(request):
    if request.user.userProfile.department >= 6:
        postFilter = BBSPosts.objects.filter(priority = 1)
    else:
        postFilter = BBSPosts.objects.filter(priority = 1, department = request.user.userProfile.department)
    stickyPosts = BBSPosts.objects.filter(priority = 2)
    storewidePosts = BBSPosts.objects.filter(department = 8)
    # paginator = Paginator(postFilter, 10)

    context = {
        'deptList': departments,
        'eventList': storeEvent.objects.order_by('-start_date'),
        'postList': postFilter,
        'storewidePosts': storewidePosts,
        'stickyPosts': stickyPosts,
    }
    return render(request, 'bbs/main.html', context)