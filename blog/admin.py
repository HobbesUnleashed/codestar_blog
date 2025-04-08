from django.contrib import admin

# Import the below to allow us to access the models as admins
from .models import Post

# Register your models here.

# Code to allow access to all posts
admin.site.register(Post)
