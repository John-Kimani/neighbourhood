from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from users.models import Profile


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
    
    @classmethod
    def display_neighborhoods(cls):
        '''
        Function that displays neighborhoods
        '''
        neighborhoods = cls.objects.all()
        return neighborhoods

    @classmethod
    def get_hood(cls, pk):
        return cls.objects.get(id=pk)

class Business(models.Model):
    '''
    Businesses class
    '''
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    contact = models.EmailField()
    neighborhood = models.ForeignKey(Neighborhood, null=True, blank=True, on_delete=models.CASCADE)
    description = models.TextField()
    business_img = CloudinaryField('images/')

    def __str__(self):
        return self.name
    
    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()
    
    @classmethod
    def display_business(cls):
        business = cls.objects.all()
        return business
    

class Post(models.Model):
    '''
    Timeline messages class
    '''
    title = models.CharField(max_length=20)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    hood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, related_name='posts')
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    hashtags = models.CharField(max_length=60, null=False, blank=True, default='#')

    def __str__(self):
        return self.title

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()