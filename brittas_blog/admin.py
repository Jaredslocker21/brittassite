from django.contrib import admin
from django.utils.html import format_html
from .models import HomePageContent, Jewelry, Painting, Sculpture

class HomePageContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'display_image')

    def short_description(self, obj):
        return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description
    short_description.short_description = 'Description'

    def display_image(self, obj):
        return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />', obj.image.url)
    display_image.allow_tags = True
    display_image.short_description = 'Image'

class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description', 'display_image')
    search_fields = ('name', 'description')
    list_filter = ('name',)

    def short_description(self, obj):
        return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description
    short_description.short_description = 'Description'

    def display_image(self, obj):
        return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />', obj.image.url)
    display_image.allow_tags = True
    display_image.short_description = 'Image'

admin.site.register(HomePageContent, HomePageContentAdmin)
admin.site.register(Jewelry, GalleryItemAdmin)
admin.site.register(Painting, GalleryItemAdmin)
admin.site.register(Sculpture, GalleryItemAdmin)
