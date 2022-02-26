
from django.shortcuts import render
from .models import Image,Category,Location



# Create your views here.
posts=[
    
    {'category':'Adventure',
     'image':'epic',
    #  'location':'Nairobi',
     },
    {'category':'Nature',
     'image':'fashion',
     'location':'Hawaii',
     },
    {'category':'Research',
     'image':'documental',
     'location':'Arusha',
     },
     
]

def home(request):
    context={'posts':Image.objects.all()}
    return render (request,'home.html',context)

# def post(request):
#     context={'':}
#     return render(request,'postform.html',context)
    