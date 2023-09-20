from django.db import models
from datetime import datetime

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_created = models.DateTimeField(default=datetime.now())
    image = models.ImageField(upload_to='static/blog')


class BlogComment(models.Model):
    created_by = models.CharField(max_length=100, verbose_name="Name")
    created_email = models.EmailField(max_length=255, verbose_name="Email")
    content = models.CharField(max_length=1000)
    post_date = models.DateTimeField(default=datetime.now())
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

