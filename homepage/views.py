from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from .models import Blogs
from .models import Destination
from .models import Testimonials
from django.db.models import Q
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


def description(request, desc_id):
    my_blogs = Blogs.objects.get(id=desc_id)
    template = loader.get_template('description.html')
    context = {
        'my_blogs': my_blogs,
    }
    return HttpResponse(template.render(context, request))


def travel(request):
    name = request.GET['name']
    budget = request.GET['budget']
    if name and budget in request.GET:
        multiple_search = Q(Q(name__icontains=name) | Q(price__icontains=budget))
        destination = Destination.objects.filter(multiple_search)
    else:
        destination = Destination.objects.filter(name__icontains=name)

    my_blogs = Blogs.objects.all().values()
    testimonials = Testimonials.objects.all().values()
    template = loader.get_template('homepage.html')
    context = {
        'my_blogs': my_blogs,
        'destination': destination,
        'testimonials': testimonials,
        'media_url': MEDIA_URL
    }
    return HttpResponse(template.render(context, request))
