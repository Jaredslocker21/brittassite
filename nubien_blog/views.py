from django.shortcuts import render, get_object_or_404  #nubien_blog views.py
from .models import Service, BlogPost, HomePageContent

def home(request):
    return render(request, 'home.html')

def about(request, id=None):
    # Fetch the first piece of content for the about page
    home_content = HomePageContent.objects.first()  # Fetches the first content
    
    if id:
        # Fetch a specific blog post if an id is passed
        blog_post = get_object_or_404(BlogPost, id=id)
        return render(request, 'about.html', {'home_content': home_content, 'blog_posts': [blog_post]})
    
    # Otherwise, fetch all blog posts
    blog_posts = BlogPost.objects.all()
    return render(request, 'about.html', {'home_content': home_content, 'blog_posts': blog_posts})

def contact(request):
    return render(request, 'contact.html')

def services(request):
    services = Service.objects.all()  # Fetch all services
    return render(request, 'services.html', {'services': services})
