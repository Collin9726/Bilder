from django.db import models

# Create your models here.
class Location(models.Model):
    location_name= models.CharField(max_length =30)

    def __str__(self):
        return self.location_name 

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location(self):
        pass



class Category(models.Model):
    category_name= models.CharField(max_length =30) 

    def __str__(self):
        return self.category_name 

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self):
        pass



class Image(models.Model):    
    post_date = models.DateTimeField(auto_now_add=True)
    image_url = models.ImageField(upload_to = 'posts/')
    image_name = models.CharField(max_length =30)
    image_description = models.TextField()
    image_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    image_category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        pass

    @classmethod
    def get_image_by_id(cls,id):
        result = cls.objects.get(id = id)
        return result

    @classmethod
    def search_images(cls, cat):
        photos = cls.objects.filter(image_category=cat)
        return photos    

    def filter_by_location(cls, location):
        pass
