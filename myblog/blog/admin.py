from django.contrib import admin
from .models import Post, Comment, MyUser
from django.contrib.auth.admin import UserAdmin

class CommentsInline(admin.TabularInline):
    model = Comment
    extra = 0


class PostInline(admin.StackedInline):
    model = Post
    extra = 0
    fields = (('author', 'title'), 'text', 'modified_date')
    show_change_link = True



class PostAdmin(admin.ModelAdmin):
    fields = (('author', 'title'), 'text', 'modified_date')
    inlines = (CommentsInline,)


class UserAdmin(admin.ModelAdmin):
    fields = ('username', ('first_name', 'last_name'))
    inlines = (PostInline, )

class CommentAdmin(admin.ModelAdmin):
    show_change_link = True


admin.site.register(MyUser, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)


# admin.site.register(Author)
# admin.site.register(Blog)
# admin.site.register(Entry)

# Register your models here.
