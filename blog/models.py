from django.db import models
from django.contrib.auth.models import User

# Tuple for constant STATUS - 0=Draft, 1=Published
STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    # One user can make many posts - but when user is deleted, so are ALL their posts
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    # Uses a constant of STATUS - built as a Tuple above the class
    status = models.IntegerField(choices=STATUS, default=0)
