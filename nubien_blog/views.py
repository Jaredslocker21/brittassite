from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def service_list(request):
    # Logic to fetch and display services
    return render(request, 'services/service_list.html')

def service_detail(request, pk):
    # Logic to fetch and display a specific service by pk
    return render(request, 'services/service_detail.html')

def service_create(request):
    # Logic for creating a new service
    return render(request, 'services/service_form.html')

def service_update(request, pk):
    # Logic for updating an existing service
    return render(request, 'services/service_form.html')

def service_delete(request, pk):
    # Logic for deleting a service
    return render(request, 'services/service_confirm_delete.html')

def blog_list(request):
    # Logic to fetch and display blog posts
    return render(request, 'blog/blog_list.html')

def blog_detail(request, pk):
    # Logic to fetch and display a specific blog post by pk
    return render(request, 'blog/blog_detail.html')

from django.shortcuts import render

def contact(request):
    return render(request, 'contact.html')  # Make sure to create this template

