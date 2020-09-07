from django.contrib import admin

from .models import Keyword, KeywordSet, ImageType, ImageEntry

@admin.register(Keyword)
class Keyword(admin.ModelAdmin):
    pass

@admin.register(KeywordSet)
class KeywordSet(admin.ModelAdmin):
    pass

@admin.register(ImageType)
class ImageType(admin.ModelAdmin):
    pass

@admin.register(ImageEntry)
class ImageEntry(admin.ModelAdmin):
    pass