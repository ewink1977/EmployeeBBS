from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from posts.models import BBSPosts, BBSReply

def viewSinglePost(request, postID):
    pass

def viewReply(request, postID, replyID):
    pass

def createNewPost(request):
    userPosting = request.user
    if request.user.userProfile.department >= 6:
        postFilter = BBSPosts.objects.filter(priority = 1)
    else:
        postFilter = BBSPosts.objects.filter(priority = 1, department = request.user.userProfile.department)
    stickyPosts = BBSPosts.objects.filter(priority = 2)
    storewidePosts = BBSPosts.objects.filter(department = 8)
    context = {
        'postList': postFilter,
        'storewidePosts': storewidePosts,
        'stickyPosts': stickyPosts,
    }

    if not request.POST['bbsPostDepartment']:
        newPost = BBSPosts.objects.create(
            author = userPosting,
            content = request.POST['bbsPostMessage']
        )
        newPost.save()
        return render(request, 'posts/partial_newpost_return.html', context)
    else:
        newPost = BBSPosts.objects.create(
            author = userPosting,
            content = request.POST['bbsPostMessage'],
            priority = request.POST['bbsPostPriority'],
            department = request.POST['bbsPostDepartment']
        )
        newPost.save()
        return render(request, 'posts/partial_newpost_return.html', context)

def replyToPost(request):
    pass

def likePost(request, postID):
    pass
