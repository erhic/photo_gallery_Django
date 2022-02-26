from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home-images' ),
    path('upload/',views.post,name='post-images' ),
   
]
