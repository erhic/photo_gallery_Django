
from django.shortcuts import render,redirect
from .models import Image,Category,Location
from .form import ImageForm



# Create your views here.
# posts=[
    
#     {'category':'Adventure',
#      'image':'epic',
#     #  'location':'Nairobi',
#      },
#     {'category':'Nature',
#      'image':'fashion',
#      'location':'Hawaii',
#      },
#     {'category':'Research',
#      'image':'documental',
#      'location':'Arusha',
#      },
     
# ]

def home(request):
    form=ImageForm()
    images = Image.objects.all().order_by('-id')
    location = Location.objects.all()
    categories = Category.objects.all()
    context={'images': images, 'locations': location, 'categories': categories}
    return render (request,'home.html',context)

