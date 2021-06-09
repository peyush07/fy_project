from django import forms
from .models import BD_Image 

class BD_ImageForm(forms.ModelForm):
    class Meta:
        model = BD_Image
        fields = ['pre_image', 'post_image', 'output_image']
        widgets = {
            'pre_image': forms.FileInput(attrs={'class': 'form-control'}),
            'post_image': forms.FileInput(attrs={'class': 'form-control'}),
            'output_image': forms.HiddenInput()
            }
    