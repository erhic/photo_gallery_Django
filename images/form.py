from dataclasses import field
from django.forms import ModelForm
from .models import Image,Category,Location


class ImageForm(ModelForm):
    class Meta:
        model=Image
        field='__all__'