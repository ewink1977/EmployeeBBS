from django.urls import path
from posts import views as postViews


urlpatterns = [
    path('create/', postViews.createNewPost, name = 'createPost'),
    path('partial/', postViews.partialPostReturn, name = 'partialReturn'),
    path('<postID>/', postViews.viewSinglePost, name = 'postView'),
    path('<postID>/<replyID>/', postViews.viewReply, name = 'viewReply'),
    path('<postID>/create_reply/', postViews.replyToPost, name = 'replyToPost'),
    path('<postID>/like/', postViews.likePost, name = 'likePost')
]