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


def display_photo(request, photo_id):
    categories=Category.objects.all()
    locations=Location.objects.all()
    try:
        photo = Image.objects.get(id = photo_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"photo.html", {"photo":photo, "categories": categories, "locations": locations})
