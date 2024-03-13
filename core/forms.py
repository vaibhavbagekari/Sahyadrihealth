from django import forms
from .models import Hospital_Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Hospital_Image
        fields = ['user','title', 'image']