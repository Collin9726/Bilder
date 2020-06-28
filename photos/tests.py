from django.test import TestCase
from .models import Image, Location, Category

# Create your tests here.
class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.this_location = Location(location_name='Lodwar')
        self.this_category = Category(category_name='Safari')
        self.this_image = Image(image_name = 'myimage', image_description ='messi is back playing football', image_location=self.this_location, image_category=self.this_category)

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.this_image,Image))
