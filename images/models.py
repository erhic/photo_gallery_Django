from email.mime import image
from time import timezone
from turtle import mode
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Image(models.Model):
    image=models.FileField()
    image_name=models.CharField(max_length=150)
    image_descr=models.TextField(max_length=1000)
    image_location=models.ForeignKey('Category',on_delete=models.SET_NULL)
    image_category=models.ForeignKey('Location',on_delete=models.SET_NULL)
    user=models.ForeignKey(User )
    date_posted=models.DateTimeField(default=timezone.now)
    time_posted=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.image_name
    
class Category(models.Model):
    category=models.TextField(max_length=150)
    
    def __str__(self):
        return self.image_name
    

    
    
class Location(models.Model):
    location=models.TextField(max_length=250)
    
    def __str__(self):
        return self.image_name