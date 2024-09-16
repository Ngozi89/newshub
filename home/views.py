from django.shortcuts import render
from django.views import generic, View
from .models import Post


# Create your views here.
class Home(generic.TemplateView):
    """This view is used to display the home page"""
    template_name = "index.html"


class PostList(generic.ListView):
    model = Post
# Render list of post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'news.html'
# Seperate the pages
    paginate_by = 8
