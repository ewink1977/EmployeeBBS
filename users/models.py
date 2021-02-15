from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
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

    # Creating a user will automatically create a profile!

    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         UserProfile.objects.create(user=instance)

    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()
