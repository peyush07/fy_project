from django import forms
from .models import BD_fixedModel

class BD_fixedForm(forms.ModelForm):
    class Meta:
        model = BD_fixedModel
        fields = ['disasters', 'base_path']
        widgets = {
            'disasters': forms.FileInput(attrs={'class': 'form-control'}),
            'base_path': forms.HiddenInput()
            }

    