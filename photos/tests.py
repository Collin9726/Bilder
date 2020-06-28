from django.test import TestCase
from .models import Image, Location, Category

# Create your tests here.
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
        photo = Image.objects.get(id = 1)
        photo.delete_image()
        photos = Image.objects.all()
        self.assertTrue(len(photos) == 0)
