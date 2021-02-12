from django.db import models
from django.contrib.auth.models import User

class storeEvent(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    department = models.IntegerField(default = 8)
    poster = models.ForeignKey(
        User,
        related_name = 'eventPost',
        on_delete = models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)