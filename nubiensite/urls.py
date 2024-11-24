from django.contrib import admin
from django.urls import path
from nubien_blog.views import home, services, about
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('services/', services, name='services'),
    path('about/', about, name='about'),
    path('contact/', about, name='contact'),  # Fix: Changed 'art' to 'about'
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)