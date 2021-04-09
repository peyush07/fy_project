from django.shortcuts import render
from django.views.generic import TemplateView
from employee.views import EmployeeImage, EmpImageDisplay
from BD_detection.views import BD_SelectImageView, BD_output

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

