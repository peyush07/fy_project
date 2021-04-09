from django.db import models

# disasters = (
#     ('gvol','guatemala-volcano'),
#     ('ptsu', 'palu-tsunami'),
#     ('harvey', 'hurricane-harvey'),
#     ('srwf', 'santa-rosa-wildfire'),
# )

# Create your models here.
class BD_Image(models.Model):
    pre_image = models.ImageField(upload_to = 'upload2/')
    post_image = models.ImageField(upload_to = 'upload2/')
    output_image = models.ImageField( blank = True)


