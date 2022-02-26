
from time import timezone
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Image(models.Model):
    name=models.CharField(max_length=150)
    image=models.FileField()
    descr=models.TextField(max_length=1000)
    location=models.ForeignKey('Location',on_delete=models.SET_NULL,null=True)
    category=models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    user=models.ForeignKey(User ,on_delete=models.CASCADE)
    date_posted=models.DateTimeField(default=timezone.now)
    time_posted=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    category=models.TextField(max_length=150)
    
    def __str__(self):
        return self.category
    

    
    
class Location(models.Model):
    location=models.TextField(max_length=250)
    
    def __str__(self):
        return self.location