from django.contrib import admin
from .models import Artist, Album

# Register your models here.
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    pass

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    pass
