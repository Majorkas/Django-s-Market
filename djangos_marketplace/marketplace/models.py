from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

from cloudinary_storage.storage import MediaCloudinaryStorage
from cloudinary.utils import cloudinary_url
from django.templatetags.static import static


User = get_user_model()

class MarketItem(models.Model):
    title = models.CharField(max_length=20,)
    image = models.ImageField(upload_to='item_pics', storage=MediaCloudinaryStorage(),null=True,)
    price = models.IntegerField()
    contact = models.CharField(max_length=30, default='Not Provided')
    description = models.TextField()
    is_available = models.BooleanField(default=True)
    date_posted = models.DateTimeField(default=timezone.now)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='market_item')

    def __str__(self):
        return self.title
