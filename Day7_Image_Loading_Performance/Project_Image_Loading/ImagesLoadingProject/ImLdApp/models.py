from django.db import models

# Create your models here.
# models.py

from django.db import models

class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description
