from django.shortcuts import render
from blog.models import Post
# from django.http import HttpResponse

# posts = [
#     {
#         'author': 'Byom',
#         'title': 'Blog post 1',
#         'content': 'First post content',
#         'date_posted': 'September 12, 2020'
#     },
#     {
#         'author': 'Sachin',
#         'title': 'Blog post 2',
#         'content': 'Second post content',
#         'date_posted': 'September 10, 2020'
#     }
# ]

def home(request):
    # return HttpResponse('<h1>Blog Home</h1>')
    # context = {
    #     'posts': posts
    # }
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    # return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})