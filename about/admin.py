from django.contrib import admin
from .models import About
from .models import Team

# Register your models here.


class AboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'description', 'email')


admin.site.register(About, AboutAdmin)


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')


admin.site.register(Team, TeamAdmin)
