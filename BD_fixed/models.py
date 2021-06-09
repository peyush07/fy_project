from django.db import models

# Create your models here.
disaster_names = (
    ('gvol','guatemala-volcano'),
    ('ptsu', 'palu-tsunami'),
    ('harvey', 'hurricane-harvey'),
    ('srwf', 'santa-rosa-wildfire'),
)
class BD_fixedModel(models.Model):
    disasters = models.CharField(max_length = 30, choices = disaster_names)
    base_path = models.CharField(max_length = 50, blank = True)
    
    # def __str__(self):
    #     return self.disasters

# class BD_SelectImages(models.Model)
#     name = models.CharField(max_length = 10)
#     disaster = models.ForeignKey(BD_fixedModel, on_delete = models.CASCADE)
    

