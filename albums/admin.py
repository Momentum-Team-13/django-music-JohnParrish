from django.contrib import admin
from .models import Album, Favorite

admin.site.register(Album)
admin.site.register(Favorite)


class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at')
