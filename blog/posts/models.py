from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=127, verbose_name="Title")
    description = models.CharField(max_length=255)
    img = models.CharField(max_length=511)
    content = models.TextField()
    created_date = models.DateField(auto_now_add=True)
