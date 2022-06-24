from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from .models import Blogs
from .models import Destination


def index(request):
    my_blogs = Blogs.objects.all().values()
    destination = Destination.objects.all().values()
    template = loader.get_template('homepage.html')
    context = {
        'my_blogs': my_blogs,
        'destination': destination,
    }
    return HttpResponse(template.render(context, request))


def description(request, id):
    my_blogs = Blogs.objects.get(id=id)
    template = loader.get_template('description.html')
    context = {
        'my_blogs': my_blogs,
    }
    return HttpResponse(template.render(context, request))


