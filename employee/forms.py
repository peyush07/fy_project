# forms.py 
from django import forms 
from .models import Employee
from .CD_model3 import run_model3

class EmployeeForm(forms.ModelForm): 
    class Meta: 
        model = Employee 
        #em = Employee.objects.filter(id=1)[0]
        fields = ['name1', 'image1','name2', 'image2', 'output_image', 'select_model', 'percentage_change']
        #find_PCAKmeans(em.emp_image1.path, em.emp_image2.path)
        widgets = {
            'name1': forms.TextInput(attrs={'class': 'form-control'}),
            'image1': forms.FileInput(attrs={'class': 'form-control'}),
            'name2': forms.TextInput(attrs={'class': 'form-control'}),
            'image2': forms.FileInput(attrs={'class': 'form-control'}),
            'select_model': forms.Select(attrs={'class': 'form-control'}),
            'output_image': forms.HiddenInput(),
            'percentage_change': forms.HiddenInput()
        }


# class CDForm(forms.ModelForm): 
#     class Meta:
#         model = ChangeDetection
#         fields = ['path1', 'path2']
