
from django.shortcuts import render,redirect
from .models import Image,Category,Location
from .form import ImageForm



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

def post(request):
    form =ImageForm()
    
    if request.method=='POST':
        form= ImageForm(request.POST)
    
    if form.is_valid():
        form.save
        return redirect ('home')
    context={'form':form}
    return render(request,'postform.html',context)
    