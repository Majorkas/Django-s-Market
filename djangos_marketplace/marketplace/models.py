from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

class Market_Item(models.Model):
    title = models.CharField(max_length=20,)
    image = models.ImageField(upload_to='item_pics')
    price = models.IntegerField()
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='market_item')
