# models.py in your Django app

from django.db import models

class HomePageContent(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='home_page_images/')
    alt_text = models.CharField(max_length=255)

    def __str__(self):
        return self.title
