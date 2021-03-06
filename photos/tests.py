from django.test import TestCase
from .models import Image, Location, Category

# Create your tests here.

class LocationTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.this_location = Location(location_name='Kisumu')

    def tearDown(self):
        Location.objects.all().delete()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.this_location,Location))

    # Testing Save Method
    def test_save_location_method(self):
        self.this_location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    # Testing Delete Method
    def test_delete_location_method(self):
        self.this_location.save_location()
        location = Location.objects.get(location_name = 'Kisumu')
        location.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)

    # Testing Update Method
    def test_update_location_method(self):
        self.this_location.save_location()
        location = Location.objects.get(location_name = 'Kisumu')        
        location.location_name = 'otherPlace'
        location.update_location()
        query_set = Location.objects.all()[:1]
        updated_location=None
        for place in query_set:
            updated_location = place
        self.assertEqual(updated_location.location_name, 'otherPlace')


class CategoryTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.this_category = Category(category_name='Workout')

    def tearDown(self):
        Category.objects.all().delete()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.this_category,Category))

    # Testing Save Method
    def test_save_category_method(self):
        self.this_category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    # Testing Delete Method
    def test_delete_category_method(self):
        self.this_category.save_category()
        category = Category.objects.get(category_name = 'Workout')
        category.delete_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 0)

    # Testing Update Method
    def test_update_category_method(self):
        self.this_category.save_category()
        category = Category.objects.get(category_name = 'Workout')     
        category.category_name = 'otherCategory'
        category.update_category()
        query_set = Category.objects.all()[:1]
        updated_category=None
        for cat in query_set:
            updated_category = cat
        self.assertEqual(updated_category.category_name, 'otherCategory')
    

class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.this_location = Location(location_name='Lodwar')
        self.this_location.save_location()
        self.this_category = Category(category_name='Safari')
        self.this_category.save_category()
        self.this_image = Image(image_name = 'myimage', image_description ='messi is back playing football', image_location=self.this_location, image_category=self.this_category)

    def tearDown(self):
        Location.objects.all().delete()
        Image.objects.all().delete()
        Category.objects.all().delete()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.this_image,Image))

    # Testing Save Method
    def test_save_image_method(self):
        self.this_image.save_image()
        photos = Image.objects.all()
        self.assertTrue(len(photos) > 0)

    # Testing Delete Method
    def test_delete_image_method(self):
        self.this_image.save_image()
        photo = Image.objects.get(image_name = 'myimage')
        photo.delete_image()
        photos = Image.objects.all()
        self.assertTrue(len(photos) == 0)

    # Testing Update Method
    def test_update_image_method(self):
        self.this_image.save_image()
        photo = Image.objects.get(image_description = 'messi is back playing football')
        photo.image_name = 'otherName'
        photo.update_image()
        photo_1 = Image.objects.get(image_description = 'messi is back playing football')
        self.assertEqual(photo_1.image_name, 'otherName')

    # Testing get_image_by_id Method
    def test_get_image_by_id_method(self):
        self.this_image.save_image()
        this_id = Image.objects.get(image_name = 'myimage').id
        photo = Image.get_image_by_id(this_id)        
        self.assertEqual(self.this_image, photo)

    # Testing filter_by_location Method
    def test_filter_by_location_method(self):
        self.this_image.save_image()        
        query_set = Image.filter_by_location(self.this_location)
        photo=None
        for pic in query_set:
            photo = pic        
        self.assertEqual(self.this_image, photo)

    # Testing search_images Method
    def test_search_images_method(self):
        self.this_image.save_image()        
        query_set = Image.search_images(self.this_category)
        photo=None
        for pic in query_set:
            photo = pic        
        self.assertEqual(self.this_image, photo)

    
