from django.shortcuts import render
from .models import Image, Category, Location

# Create your views here.
def welcome(request):  
    categories=Category.objects.all()
    locations=Location.objects.all()  
    
    return render(request, 'welcome.html', {"categories": categories, "locations": locations})

def home(request):
    pics=[]
    categories=Category.objects.all()
    locations=Location.objects.all()
    for cat in categories:
        photos=Image.objects.filter(image_category = cat)
        pics.append(photos)
    
    return render(request, 'all.html', {"pics": pics, "categories": categories, "locations": locations})

