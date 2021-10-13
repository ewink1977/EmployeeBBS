from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        related_name = 'userProfile',
        on_delete = models.CASCADE
        )
    position = models.CharField(max_length = 255, blank = True)
    bio = models.TextField(blank = True)
    image = ProcessedImageField(default = 'media/profilePics/default.jpg', 
        upload_to='media/profilePics', 
        processors=[ResizeToFit(500, 500)], 
        format='JPEG', 
        options={'quality': 80}
        )
    department = models.IntegerField(default = 1)
    access_level = models.IntegerField(default = 1)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.user.username}'s profile!"

class UserTimeManagement(models.Model):
    user = models.ForeignKey(
        User,
        related_name = 'userTimeClock',
        on_delete = models.CASCADE
    )
    clocked_in = models.BooleanField(default = False)
    time_in = models.DateTimeField(blank = True, null = True, default = timezone.now)
    time_out = models.DateTimeField(blank = True, null = True, default = timezone.now)
    total = models.DurationField(blank = True, null = True)
    note = models.CharField(max_length = 255, blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

