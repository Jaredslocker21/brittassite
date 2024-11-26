from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nubien_blog.urls')),  # Correctly include the app's URLs
]
