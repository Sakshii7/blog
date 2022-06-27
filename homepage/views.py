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
    if 'name' or 'budget' in request.GET:
        search = request.GET['name']
        budget = request.GET['budget']
        multiple_search = Q(Q(name__icontains=search) | Q(price__icontains=budget))
        destination = Destination.objects.filter(multiple_search)
    # elif 'budget' in request.GET:
    #     budget = request.GET['budget']
    #     destination = Destination.objects.filter(price__icontains=budget)
    else:
        destination = Destination.objects.all().values()

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


def description(request, id):
    my_blogs = Blogs.objects.get(id=id)
    template = loader.get_template('description.html')
    context = {
        'my_blogs': my_blogs,
    }
    return HttpResponse(template.render(context, request))
