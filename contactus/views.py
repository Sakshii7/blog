from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Contact


def contact_page(request):
    template = loader.get_template('form.html')
    return HttpResponse(template.render({}, request))


def add_contact(request):
    name = request.POST['name']
    email = request.POST['email']
    mobile = request.POST['mobile']
    query = request.POST['query']

    contact = Contact(name=name, email=email, mobile=mobile, query=query)
    contact.save()
    return HttpResponseRedirect(reverse('contact'))
