from django.db import models


model_choices = (
    ('PcaKmeans', 'PCA K-means'),
    ('vgg19','VGG19'),    
)

class Employee(models.Model):
    name1 = models.CharField(max_length=50, blank=True)
    image1 = models.ImageField(upload_to='upload/')
    name2 = models.CharField(max_length=50, blank=True)    
    image2 = models.ImageField(upload_to='upload/')
    output_image = models.CharField(max_length=1000, blank=True)
    select_model = models.CharField(max_length=20, choices=model_choices, default='PcaKmeans')
    percentage_change = models.CharField(max_length=1000, blank=True)

# class ChangeDetection(models.Model):
#     em = Employee.objects.filter(id=1)[0]
#     path_1 = em.emp_image1.path
#     path_2 = em.emp_image2.path
    
    
    