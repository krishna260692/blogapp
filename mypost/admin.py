from django.contrib import admin

# Register your models here.

from .models import Post,Newpost

admin.site.register(Post)

admin.site.register(Newpost)
