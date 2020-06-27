from django.shortcuts import render
from .models import Image, Category, Location

# Create your views here.
def welcome(request):  
    categories=Category.objects.all()
    locations=Location.objects.all()  
    
    return render(request, 'welcome.html', {"categories": categories, "locations": locations})


def all_photos(request):
    categories=Category.objects.all()
    locations=Location.objects.all()
    pics=Image.objects.all().order_by('-post_date')
    
    return render(request, 'all-photos.html', {"pics": pics, "categories": categories, "locations": locations})


def all_categories(request):
    pics=[]
    categories=Category.objects.all()
    locations=Location.objects.all()
    for cat in categories:
        photos=Image.objects.filter(image_category = cat)
        pics.append(photos)
    
    return render(request, 'all-categories.html', {"pics": pics, "categories": categories, "locations": locations})


def display_photo(request, photo_id):
    categories=Category.objects.all()
    locations=Location.objects.all()
    try:
        photo = Image.objects.get(id = photo_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"photo.html", {"photo":photo, "categories": categories, "locations": locations})


def display_category(request, cat_id):
    categories=Category.objects.all()
    locations=Location.objects.all()
    try:
        cat = Category.objects.get(id = cat_id)
    except DoesNotExist:
        raise Http404()

    photos=Image.objects.filter(image_category = cat)

    return render(request,"category.html", {"photos":photos, "category":cat, "categories": categories, "locations": locations})
