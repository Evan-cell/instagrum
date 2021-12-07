from django.contrib import admin
from models import Post, Tag, Follow

# Register your models here.
admin.site.register(Post,Tag,Follow)
