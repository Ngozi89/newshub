from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django_extensions.db.fields import AutoSlugField


STATUS = ((0, "Draft"), (1, "Pulished"))

# Create post models.
class Post(models.Model):
    title = models.CharField(max_length=120, unique=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="news_post")
    updated_on = models.DateTimeField(auto_now=True)
    subtitle = models.CharField(max_length=150, null=True)
    content = models.TextField(blank=True, null=True)
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='home_like', blank=True)

    class Meta:
        """To diaplay the news by created on in decending order"""
        ordering = ["-created_on"]
        
    # Add string that returns representation of an object.
    def __str__(self):
        return f"{self.title}"
        
    # Returns total number of likes on a post.
    def number_of_likes(self):
        return self.likes.count()


# Add comment models.
class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
        