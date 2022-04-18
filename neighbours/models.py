from django.db import models
from cloudinary.models import CloudinaryField


class Neighborhood(models.Model):
    '''
    Neighborhood class
    '''
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    description = models.TextField()
    hood_img = CloudinaryField('images/')

    def __str__(self):
        return self.name

    def save_neighborhood(self):
        self.save()
    
    def delete_neighborhood(self):
        self.delete()
