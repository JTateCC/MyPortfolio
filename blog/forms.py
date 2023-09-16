from django.forms import ModelForm
from blog.models import BlogComment

class BlogSubmitForm(ModelForm):
    class Meta:
        model = BlogComment
        fields = ['created_by', 'created_email', 'post_date']
