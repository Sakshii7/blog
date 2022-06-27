from django.contrib import admin
from .models import Blogs, Destination, Testimonials


# Register your models here.


class BlogsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')


class DestinationsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image', 'offer')


class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


admin.site.register(Blogs, BlogsAdmin)
admin.site.register(Destination, DestinationsAdmin)
admin.site.register(Testimonials, TestimonialsAdmin)
