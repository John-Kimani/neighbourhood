from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone


class Profile(models.Model):
    '''
    User class that provides user profile
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = CloudinaryField('images/', default='https://res.cloudinary.com/dbgbail9r/image/upload/v1649544556/profile_image_kfrlhw.png')
    bio = models.TextField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_joined = models.DateField(default=timezone.now)

    def __str__(self):
        return self.user.username


