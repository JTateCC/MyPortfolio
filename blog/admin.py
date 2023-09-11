from django.contrib import admin

# Register your models here.
from blog.models import BlogPost, BlogComment

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(BlogComment)