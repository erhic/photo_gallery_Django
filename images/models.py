import cloudinary
from cloudinary.models import CloudinaryField
from distutils.command.upload import upload
from time import timezone
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Image(models.Model):
    name=models.CharField(max_length=150)
    image = CloudinaryField('image')
    description=models.TextField(max_length=1000)
    location=models.ForeignKey('Location',on_delete=models.SET_NULL,null=True)
    category=models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    # user=models.ForeignKey(User ,on_delete=models.CASCADE)
    # date_posted=models.DateTimeField(default=timezone.now)
    time_posted=models.DateTimeField(auto_now_add=True)
    
    # save image to database
    def save_image(self):
        self.save()


    # update image
    def update_image(self, name, description, location, category):
        self.name = name
        self.description = description
        self.location = location
        self.category = category
        self.save()

    # get all images
    @classmethod
    def get_all_images(cls):
        images = Image.objects.all()
        return images

    # get image by id
    @classmethod
    def get_image_by_id(cls, id):
        image = Image.objects.get(id=id)
        return image

    # get images by location
    @classmethod
    def filter_by_location(cls, location):
        images = Image.objects.filter(location__name=location)
        return images

    # get images by category
    @classmethod
    def filter_by_category(cls, category):
        images = Image.objects.filter(category__name=category)
        return images

    # search images
    @classmethod
    def search_image(cls, search_by):
        images = cls.objects.filter(name__icontains=search_by)
        return images

    # delete image from database
    def delete_image(self):
        self.delete()

    def __str__(self):
        return self.name
    
    
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name=models.TextField(max_length=150)
    
    # save category to database
    def save_category(self):
        self.save()

    # update category
    def update_category(self, name):
        self.name = name
        self.save()

    # delete category from database
    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.name

    
    
    

    
    
class Location(models.Model):
    name =models.TextField(max_length=250)
    
    # save location to database
    def save_location(self):
        self.save()

    # update location
    def update_location(self, name):
        self.name = name
        self.save()

     # delete location from database
    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name



