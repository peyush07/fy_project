from django.urls import path
from .views import HomePageView, AboutPageView, EmployeeImage, EmpImageDisplay, BD_SelectImageView
from .views import BD_output, BD_fixedView1, BD_fixedView2, BD_fixedView3
# , BD_fixedOutputView
# , BD_pageView, BD_fixedView

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('about/', AboutPageView.as_view(), name = 'about'),
    path('emp_image/', EmployeeImage.as_view(), name = 'emp_image.html'),
    path('upload/<int:pk>/', EmpImageDisplay.as_view(), name='emp_image_display'),
    # path('BD_page/', BD_pageView.as_view(), name='BD_page.html'),
    path('BD_selectImage/', BD_SelectImageView.as_view(), name = 'BD_selectImage.html'),
    path('upload2/<int:pk>/', BD_output.as_view(), name = 'BD_output_display'),
    # path('BD_fixed/', BD_fixedView.as_view(), name='BD_fixed.html'),
    # path('BD_fixedOutput/', BD_fixedOutputView.as_view(), name='BD_fixedOutput.html'),
    # path('BD_selectDisaster/', BD_fixedView.as_view(), name = 'BD_selectDisaster.html'),
    # path('<int:pk>/', BD_fixedOutputView.as_view(), name = 'BD_fixedOutput'),
    path('BD_fixed/', BD_fixedView1.select_disaster, name = 'BD_fixed.html'),
    path('get_images/', BD_fixedView2.get_images, name = 'bd2.html'),
    path('getOutput/', BD_fixedView2.getOutput, name = 'getOutput'),
]

app_name = 'home'