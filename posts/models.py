import uuid
from django.db import models
from django.contrib.auth.models import User

class BBSPosts(models.Model):
    id = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False
        )
    author = models.ForeignKey(
        User,
        related_name = 'postAuthor',
        on_delete = models.CASCADE
        )
    likes = models.ManyToManyField(
        User,
        related_name = 'userLike'
    )
    content = models.TextField(max_length = 255)
    priority = models.IntegerField(default = 1)
    display_level = models.IntegerField(default = 1)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class BBSReply(BBSPosts):
    parent = models.ForeignKey(
        BBSPosts,
        on_delete = models.CASCADE
    )


