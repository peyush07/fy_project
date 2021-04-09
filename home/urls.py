from django.urls import path
from .views import HomePageView, AboutPageView, EmployeeImage, EmpImageDisplay, BD_SelectImageView, BD_output

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('about/', AboutPageView.as_view(), name = 'about'),
    path('emp_image/', EmployeeImage.as_view(), name = 'emp_image.html'),
    path('upload/<int:pk>/', EmpImageDisplay.as_view(), name='emp_image_display'),
    path('BD_selectImage/', BD_SelectImageView.as_view(), name = 'BD_selectImage.html'),
    path('upload2/<int:pk>/', BD_output.as_view(), name = 'BD_output_display')
]

app_name = 'home'