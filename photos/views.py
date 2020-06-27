from django.shortcuts import render
from .models import Image, Category

# Create your views here.
def welcome(request):    
    
    return render(request, 'welcome.html')

def home(request):
    pics=[]
    categories=Category.objects.all()
    for cat in categories:
        photos=Image.objects.filter(image_category = cat)
        pics.append(photos)
    
    return render(request, 'all.html', {"pics": pics})

