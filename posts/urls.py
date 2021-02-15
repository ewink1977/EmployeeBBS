from django.urls import path
from posts import views as postViews

urlpatterns = [
    path('create/', postViews.createNewPost, name = 'createPost'),
    path('partial/', postViews.partialPostReturn, name = 'partialReturn'),
    path('reply/', postViews.replyPost, name = 'replyPost'),
    path('like/<postID>/', postViews.likePost, name = 'likePost'),
    path('del/post/<postID>/', postViews.deletePostConfirm, name = 'deletePost'),
    path('del/reply/<postID>/', postViews.deleteReplyConfirm, name = 'deleteReply'),
    path('del/post/confirm/<postID>', postViews.deletePostFinal, name = 'deletePostFinal'),
    path('del/reply/confirm/<postID>', postViews.deleteReplyFinal, name = 'deleteReplyFinal'),
    path('<postID>/', postViews.viewSinglePost, name = 'postView'),
]