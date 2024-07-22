from django.contrib.auth.models import User
from django.db import models

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=31)
    rating = models.IntegerField(default=0)
    image = models.ImageField(upload_to='feedback_images/', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    food = models.IntegerField(null=True)