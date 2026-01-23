from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField





class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = CloudinaryField('image', blank=True, null=True, folder='profile_pictures/', transformation={
            'width': 200,
            'height': 200,
            'crop': 'fill',
            'gravity': 'face',
            'quality': 'auto',
            'fetch_format': 'auto'
        } )


    def __str__(self):
        return f"{self.user.username}'s Profile"
