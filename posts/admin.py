from django.contrib import admin
from .models import Post, Like, Bookmark

# Register your models here.

admin.site.register(Bookmark)
admin.site.register(Like)
admin.site.register(Post)