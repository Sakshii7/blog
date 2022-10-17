from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from .models import *
from blogs.settings import MEDIA_URL


def about_index(request):
    about = About.objects.all().values()
    team = Team.objects.all().values()
    template = loader.get_template('about_view.html')
    context = {
        'about': about,
        'team': team,
        'media_url': MEDIA_URL
    }
    return HttpResponse(template.render(context, request))
