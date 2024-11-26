# nubien_blog/urls.py

from django.urls import path
from . import views  # Import the views from the current app (nubien_blog)

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.service_list, name='services'),
    path('services/', views.service_list, name='service_list'),
    path('services/<int:pk>/', views.service_detail, name='service_detail'),
    path('services/new/', views.service_create, name='service_create'),
    path('services/<int:pk>/edit/', views.service_update, name='service_update'),
    path('services/<int:pk>/delete/', views.service_delete, name='service_delete'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('about/', views.about, name='about'),  # Assuming 'about' is a view in views.py
    path('contact/', views.contact, name='contact'),  # Assuming 'contact' is a view in views.py
]
