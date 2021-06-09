from django.shortcuts import render
from django.views.generic import TemplateView
from employee.views import EmployeeImage, EmpImageDisplay
from BD_detection.views import BD_SelectImageView, BD_output
from BD_fixed.views import BD_fixedView1, BD_fixedView2, BD_fixedView3
# , BD_fixedOutputView
# , BD_pageView, BD_fixedView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'
