from email.mime import image
from time import timezone
from turtle import mode
from django.db import models
from django.utils import timezone

# Create your models here.
class Image(models.Model):
    image=models.FileField()
    image_name=models.CharField(max_length=150)
    image_descr=models.TextField(max_length=1000)
    image_location=models.TextField(max_length=200)
    image_category=models.TextField(max_length=200)
    date_posted=models.DateTimeField(default=timezone.now)
    time_posted=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.image_name
    
    
class Category(models.Model):
    category=models.TextField(max_length=150)
    
    def __str__(self):
        return self.image_name
    
    
class location(models.Model):
    location=models.TextField(max_length=250)
    
    def __str__(self):
        return self.image_name