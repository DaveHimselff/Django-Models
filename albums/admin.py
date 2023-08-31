from django.contrib import admin
from .models import Musician, Album
from .models import Tag, Category, Article
# Register your models here.

admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Article)

@admin.register(Musician)
class MusicianADmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name',)
    list_display = ('first_name', 'last_name',)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('__str__', 'name', 'release_date',)