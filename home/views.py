from django.shortcuts import render, get_object_or_404, reverse
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


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked
            },
        )