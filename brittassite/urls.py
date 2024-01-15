from django.contrib import admin
from django.urls import path
from brittas_blog.views import home, jewelry, art, about
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('jewelry/', jewelry, name='jewelry'),
    path('art/', art, name='art'),
    path('about/', about, name='about'),  # Fix: Changed 'art' to 'about'
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)