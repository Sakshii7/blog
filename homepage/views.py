from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from .models import Blogs
from .models import Destination
from .models import Testimonials
from blogs.settings import MEDIA_URL


def index(request):
    my_blogs = Blogs.objects.all().values()
    destination = Destination.objects.all().values()
    testimonials = Testimonials.objects.all().values()
    template = loader.get_template('homepage.html')
    context = {
        'my_blogs': my_blogs,
        'destination': destination,
        'testimonials': testimonials,
        'media_url': MEDIA_URL
    }
    return HttpResponse(template.render(context, request))


def description(request, id):
    my_blogs = Blogs.objects.get(id=id)
    template = loader.get_template('description.html')
    context = {
        'my_blogs': my_blogs,
    }
    return HttpResponse(template.render(context, request))


