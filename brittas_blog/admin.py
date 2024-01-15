from django.contrib import admin
from .models import HomePageContent

class HomePageContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'display_image')

    def short_description(self, obj):
        return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description
    short_description.short_description = 'Description'

    def display_image(self, obj):
        return '<img src="{}" style="max-height: 50px; max-width: 50px;" />'.format(obj.image.url)
    display_image.allow_tags = True
    display_image.short_description = 'Image'

admin.site.register(HomePageContent, HomePageContentAdmin)
