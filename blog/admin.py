from django.contrib import admin

from blog.models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'user__username', 'created']
    ordering = ['-created']

admin.site.register(Post, PostAdmin)