from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    stack = models.CharField(max_length=50)
    image = models.CharField(max_length=100)
    video_link = models.CharField(max_length=100)
    github_link = models.URLField()





