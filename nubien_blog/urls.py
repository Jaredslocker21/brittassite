from django.urls import path
from . import views  # nubien_blog views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('services/', views.services, name='services'),  # Corrected to use 'services' view
    path('about/', views.about, name='about'),  # About page
    path('about/<int:id>/', views.about, name='about_detail'),  # About page with specific blog post
    path('contact/', views.contact, name='contact'),  # Contact page
]
