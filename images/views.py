from multiprocessing import context
from django.shortcuts import render


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
    context={'posts':posts}
    return render (request,'home.html',context)
    