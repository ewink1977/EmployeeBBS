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
        eventFilter = storeEvent.objects.order_by('-start_date')
    else:
        postFilter = BBSPosts.objects.filter(priority = 1, department = request.user.userProfile.department)
        eventFilter = storeEvent.objects.order_by('-start_date').filter(department = 8 or request.user.userProfile.department)
    stickyPosts = BBSPosts.objects.filter(priority = 2)
    storewidePosts = BBSPosts.objects.filter(department = 8)
    paginator = Paginator(postFilter.order_by('-created_at'), 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'deptList': departments,
        'eventList': eventFilter,
        'postList': postFilter,
        'page_obj': page_obj,
        'storewidePosts': storewidePosts,
        'stickyPosts': stickyPosts,
    }
    return render(request, 'bbs/main.html', context)