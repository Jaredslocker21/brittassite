from django.contrib import admin
from django.utils.html import mark_safe
from .models import Category, Service, BlogPost

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'created_at', 'image_thumbnail')  # Show image in list
    search_fields = ('title', 'description', 'category__name')  # Allow searching by title, description, and category
    list_filter = ('category',)  # Add filter by category
    ordering = ('-created_at',)  # Order services by creation date in descending order

    # Image thumbnail method to display in admin list
    def image_thumbnail(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" height="100" />')  # Show image preview
        return 'No Image'  # Fallback if no image is available

    image_thumbnail.short_description = 'Image Preview'  # Column title

    # Customize form display in the admin (optional)
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'category', 'price', 'image')
        }),
    )

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    search_fields = ('title', 'content', 'category__name')
    list_filter = ('category',)
