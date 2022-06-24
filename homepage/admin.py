from django.contrib import admin
from .models import Blogs, Destination


# Register your models here.


class BlogsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')


class DestinationsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'offer')


admin.site.register(Blogs, BlogsAdmin)
admin.site.register(Destination, DestinationsAdmin)
