from django.db import models
from django.contrib.auth.models import AbstractUser


class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def check_is_user_favorite(self, user):
        for favorite in self.favorites.all():
            if favorite.album == self:
                return True


class User(AbstractUser):
    pass


class Favorite(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="favorites", blank=True, null=True)
    album = models.ForeignKey("Album", on_delete=models.CASCADE, related_name="favorites", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
