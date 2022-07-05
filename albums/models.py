from datetime import time
from django.db import models
from django.utils import timezone


class TimeStamp(models.Model):
    created_at = models.DateTimeField(default=timezone.now())

    class Meta:
        abstract = True


class Album(TimeStamp):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
