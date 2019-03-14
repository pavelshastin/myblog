from django.contrib import admin
from .models import Post, Author, Blog, Entry

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Blog)
admin.site.register(Entry)

# Register your models here.
