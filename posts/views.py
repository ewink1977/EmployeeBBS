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
    pass

def replyToPost(request):
    pass

def likePost(request, postID):
    pass
