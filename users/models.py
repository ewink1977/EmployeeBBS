from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        related_name = 'userProfile',
        on_delete = models.CASCADE
        )
    position = models.CharField(max_length = 255, blank = True)
    bio = models.TextField(blank = True)
    image = models.ImageField(default = 'default.jpg', upload_to = 'profilePics')
    department = models.IntegerField(default = 1)
    access_level = models.IntegerField(default = 1)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.user.username}'s profile!"