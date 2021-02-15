from django.urls import path
from posts import views as postViews


urlpatterns = [
    path('create/', postViews.createNewPost, name = 'createPost'),
    path('partial/', postViews.partialPostReturn, name = 'partialReturn'),
    path('<postID>/', postViews.viewSinglePost, name = 'postView'),
    path('create_reply/', postViews.replyToPost, name = 'replyToPost'),
    path('<postID>/p/delete/', postViews.deletePostConfirm, name = 'deletePost'),
    path('<postID>/r/delete/', postViews.deleteReplyConfirm, name = 'deleteReply'),
    path('delete/p/<postID>', postViews.deletePostFinal, name = 'deletePostFinal'),
    path('delete/r/<postID>', postViews.deleteReplyFinal, name = 'deleteReplyFinal'),
    path('<postID>/like/', postViews.likePost, name = 'likePost'),
]