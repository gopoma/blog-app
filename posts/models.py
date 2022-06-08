from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=127, verbose_name="Title")
    description = models.CharField(max_length=255)
    img = models.CharField(max_length=511)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # author = models.ManyToOneRel(to=User, field_name="author", field="pk", on_delete=models.SET_NULL)

    def __str__(self):
        return self.created_date.strftime("%d/%m/%Y") + " " + self.title
        # return f"{self.created_date} {self.title}"
    
    def get_absolute_url(self):
        return reverse('posts:post_detail', args=[self.pk])