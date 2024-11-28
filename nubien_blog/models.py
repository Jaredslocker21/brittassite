from django.db import models
from django.core.exceptions import ValidationError
from PIL import Image  # You can install Pillow for image processing

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

def validate_image_size(image):
    img = Image.open(image)
    max_width = 1000  # Maximum width in pixels
    max_height = 1000  # Maximum height in pixels
    if img.width > max_width or img.height > max_height:
        raise ValidationError(f"Image size should be no larger than {max_width}x{max_height} pixels.")

class Service(models.Model):
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        related_name='services'
    )
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='services/', validators=[validate_image_size])
    image_title = models.CharField(
        max_length=255,
        blank=True,
        help_text="A short descriptive title for the image."
    )
    alt_text = models.CharField(max_length=255, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.category})"



class BlogPost(models.Model):
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='blog_posts'
    )
    title = models.CharField(max_length=150)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    alt_text = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class HomePageContent(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='home_page_images/')
    alt_text = models.CharField(max_length=255)

    def __str__(self):
        return self.title
