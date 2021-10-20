from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from posts.models import BBSPosts, BBSReply

@login_required
def viewSinglePost(request, postID):
    postObj = BBSPosts.objects.get(id = postID)
    replies = BBSReply.objects.filter(parent=postObj).order_by('created_at')

    context = {
        'post_obj': postObj,
        'replies': replies,
    }
    return render(request, 'posts/post_display.html', context)

@login_required
def partialPostReturn(request):
    if request.user.userProfile.department >= 6:
        postFilter = BBSPosts.objects.filter(priority = 1, is_reply = False)
    else:
        postFilter = BBSPosts.objects.filter(priority = 1, department = request.user.userProfile.department, is_reply = False)

    stickyPosts = BBSPosts.objects.filter(
        priority=2, department=request.user.userProfile.department, is_reply = False)
    storewidePosts = BBSPosts.objects.filter(department=8, is_reply=False)

    paginator = Paginator(postFilter.order_by('-created_at'), 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'storewidePosts': storewidePosts,
        'stickyPosts': stickyPosts,
    }
    return render(request, 'posts/partial_newpost_return.html', context)

@login_required
def createNewPost(request):
    if request.method == 'POST':
        userPosting = request.user

        if request.user.userProfile.access_level == 1:
            newPost = BBSPosts.objects.create(
                author=userPosting,
                content=request.POST['bbsPostMessage'],
                priority=1,
                department=userPosting.userProfile.department,
            )
            newPost.save()

        if request.user.userProfile.access_level == 2:
            newPost = BBSPosts.objects.create(
                author = userPosting,
                content = request.POST['bbsPostMessage'],
                priority = request.POST['bbsPostPriority'],
                department = userPosting.userProfile.department,
            )
            newPost.save()
        if request.user.userProfile.access_level > 2:
            newPost = BBSPosts.objects.create(
                author = userPosting,
                content = request.POST['bbsPostMessage'],
                priority = request.POST['bbsPostPriority'],
                department = request.POST['bbsPostDepartment']
            )
            newPost.save()

        if request.user.userProfile.department >= 6:
            postFilter = BBSPosts.objects.filter(priority=1, is_reply=False)
        else:
            postFilter = BBSPosts.objects.filter(
                priority=1, department=request.user.userProfile.department, is_reply=False)

        stickyPosts = BBSPosts.objects.filter(
            priority=2, department=request.user.userProfile.department, is_reply=False)
        storewidePosts = BBSPosts.objects.filter(department=8, is_reply=False)

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

@login_required
def replyPost(request):
    if request.method == 'POST':
        parentUUID = request.POST['bbsReplyParent']
        parentPost = BBSPosts.objects.get(id = parentUUID)
        replyAuthor = request.user
        newReply = BBSReply.objects.create(
            author = replyAuthor,
            content = request.POST['bbsReplyMessage'],
            priority = 1,
            department = parentPost.department,
            is_reply = True,
            parent = parentPost,
        )
        newReply.save()
        messages.success(request, f'Nice work, @{replyAuthor.username}! Reply posted successfully!')
        return redirect('postView', parentUUID)
    else:
        messages.error(request, 'Sorry, you do not have permission to do this.', extra_tags = 'danger')
        return redirect('bbsHome')

@login_required
def likePost(request, postID):
    postToLike = BBSPosts.objects.get(id = postID)
    userLikingPost = User.objects.get(id = request.user.id)
    userLikingPost.bbsLike.add(postToLike)
    messages.success(request, f"You are a nice person for liking {postToLike.author.username}'s post!!")
    return redirect('bbsHome')

@login_required
def deletePostConfirm(request, postID):
    postToDelete = BBSPosts.objects.get(id = postID)
    context = {
        'post_obj': postToDelete,
        'postType': 1
    }
    return render(request, 'posts/confirm_delete.html', context)

@login_required
def deleteReplyConfirm(request, postID):
    replyToDelete = BBSReply.objects.get(id = postID)
    context = {
        'post_obj': replyToDelete,
        'postType': 2
        }
    return render(request, 'posts/confirm_delete.html', context)


@login_required
def deletePostFinal(request, postID):
    if request.method == 'POST':
        deletePost = BBSPosts.objects.get(id = request.POST['postID'])
        deletePost.delete()
        messages.success(request, 'Done. The post has been successfully deleted!')
        return redirect('bbsHome')
    else:
        messages.error(request, 'Sorry, you do not have permission to do this.', extra_tags = 'danger')
        return redirect('bbsHome')


@login_required
def deleteReplyFinal(request, postID):
    if request.method == 'POST':
        deleteReply = BBSReply.objects.get(id = request.POST['replyID'])
        deleteReply.delete()
        messages.success(request, 'Done. The reply has been successfully deleted!')
        return redirect('bbsHome')
    else:
        messages.error(request, 'Sorry, you do not have permission to do this.', extra_tags = 'danger')
        return redirect('bbsHome')
