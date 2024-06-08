from django.shortcuts import render
from .models import HomePageContent, Jewelry, Painting, Sculpture

def home(request):
    content = HomePageContent.objects.first()  # Retrieve the first record, modify if necessary
    return render(request, 'home.html', {'content': content})

def gallery(request):
    jewelry = Jewelry.objects.all()
    paintings = Painting.objects.all()
    sculptures = Sculpture.objects.all()
    context = {
        'jewelry': jewelry,
        'paintings': paintings,
        'sculptures': sculptures
    }
    return render(request, 'gallery.html', context)

def about(request):
    # Your view logic here
    return render(request, 'about.html')  # Replace with the actual template name
