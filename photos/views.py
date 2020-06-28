from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
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
    except Image.DoesNotExist:
        raise Http404()
    return render(request,"photo.html", {"photo":photo, "categories": categories, "locations": locations})


def display_category(request, cat_id):
    categories=Category.objects.all()
    locations=Location.objects.all()
    try:
        cat = Category.objects.get(id = cat_id)
    except Category.DoesNotExist:
        raise Http404()

    photos=Image.objects.filter(image_category = cat)

    return render(request,"category.html", {"photos":photos, "category":cat, "categories": categories, "locations": locations})


def search_categories(request):
    categories=Category.objects.all()
    locations=Location.objects.all()

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")        
        cat=None
        try:
            cat = Category.objects.get(category_name__icontains=search_term)            
        except Category.DoesNotExist:
            pass        
        
        searched_photos = Image.search_images(cat)

        message = f"{search_term}"

        return render(request, 'search.html',{"message":message, "photos": searched_photos, "categories": categories, "locations": locations})

    else:
        blank_message = "You haven't searched for any term."
        return render(request, 'search.html',{"blank_message":blank_message, "categories": categories, "locations": locations})



def display_location(request, loc_id):
    categories=Category.objects.all()
    locations=Location.objects.all()
    try:
        loc = Location.objects.get(id = loc_id)
    except Location.DoesNotExist:
        raise Http404()

    photos=Image.objects.filter(image_location = loc)

    return render(request,"location.html", {"photos":photos, "location":loc, "categories": categories, "locations": locations})


def all_locations(request):
    pics=[]
    categories=Category.objects.all()
    locations=Location.objects.all()
    for loc in locations:
        photos=Image.objects.filter(image_location = loc)
        pics.append(photos)
    
    return render(request, 'all-locations.html', {"pics": pics, "categories": categories, "locations": locations})