from django.contrib import admin
from .models import Post, self_intro, comment

# Register your models here.
admin.site.register(Post)
admin.site.register(self_intro)
admin.site.register(comment)
