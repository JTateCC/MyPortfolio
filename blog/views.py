from django.shortcuts import render
from blog.models import BlogPost, BlogComment
from blog.forms import BlogSubmitForm
# Create your views here.

def all_blogs(request):

    blogs = BlogPost.objects.all()
    return render(request, 'blog/all_blogs.html',
                  {'blogs': blogs})

def blog_detail(request, pk):
    blogpost = BlogPost.objects.get(pk=pk)
    comments = BlogComment.objects.filter(blog_post=blogpost)

    if request.method == 'POST':
        form = BlogSubmitForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.blog_post = blogpost
            new_comment.save()
    else:
        form = BlogSubmitForm()

    return render(request, 'blog/blog_detail.html', {'blogpost': blogpost,
                                                     'form' : form,
                                                     'comments' : comments})
