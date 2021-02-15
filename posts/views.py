from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from posts.models import BBSPosts, BBSReply

def viewSinglePost(request, postID):
    pass

def viewReply(request, postID, replyID):
    pass

def partialPostReturn(request):
    userPosting = request.user
    if request.user.userProfile.department >= 6:
        postFilter = BBSPosts.objects.filter(priority = 1)
    else:
        postFilter = BBSPosts.objects.filter(priority = 1, department = request.user.userProfile.department)

    stickyPosts = BBSPosts.objects.filter(priority = 2)
    storewidePosts = BBSPosts.objects.filter(department = 8)

    paginator = Paginator(postFilter.order_by('-created_at'), 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'storewidePosts': storewidePosts,
        'stickyPosts': stickyPosts,
    }
    return render(request, 'posts/partial_newpost_return.html', context)

def createNewPost(request):
    if request.method == 'POST':
        userPosting = request.user
        if request.user.userProfile.department >= 6:
            postFilter = BBSPosts.objects.filter(priority = 1)
        else:
            postFilter = BBSPosts.objects.filter(priority = 1, department = request.user.userProfile.department)

        if request.user.userProfile.access_level == 1:
            newPost = BBSPosts.objects.create(
                author = userPosting,
                content = request.POST['bbsPostMessage']
            )
            newPost.save()
        else:
            newPost = BBSPosts.objects.create(
                author = userPosting,
                content = request.POST['bbsPostMessage'],
                priority = request.POST['bbsPostPriority'],
                department = request.POST['bbsPostDepartment']
            )
            newPost.save()

        stickyPosts = BBSPosts.objects.filter(priority = 2)
        storewidePosts = BBSPosts.objects.filter(department = 8)

        paginator = Paginator(postFilter.order_by('-created_at'), 5)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'page_obj': page_obj,
            'storewidePosts': storewidePosts,
            'stickyPosts': stickyPosts,
        }
        return render(request, 'posts/partial_newpost_return.html', context)
    else:
        messages.error(request, 'Sorry, you do not have permission to do this.', extra_tags = 'danger')
        return redirect('bbsHome')

def replyToPost(request):
    pass

def likePost(request, postID):
    pass
