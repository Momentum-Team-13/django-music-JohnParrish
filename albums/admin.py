from django.contrib import admin
from .models import Album

admin.site.register(Album)


class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at')
