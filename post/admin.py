from django.contrib import admin
from post.models import Post, Category

class PostAdmin(admin.ModelAdmin):
    list_display=('title','description','pub_date')

admin.site.register(Post,PostAdmin)
