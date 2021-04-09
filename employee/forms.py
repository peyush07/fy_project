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
        widgets = {'output_image': forms.HiddenInput(),'percentage_change': forms.HiddenInput()}


# class CDForm(forms.ModelForm): 
#     class Meta:
#         model = ChangeDetection
#         fields = ['path1', 'path2']
