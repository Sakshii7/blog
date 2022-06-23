from django.shortcuts import render, redirect
import re

# Create your views here.

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Contact


def contact_page(request):
    template = loader.get_template('form.html')
    return HttpResponse(template.render({}, request))


def add_contact(request):
    regex = re.compile(
        r'(^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$)')

    name = request.POST['name']
    email = request.POST['email']
    mobile = request.POST['mobile']
    query = request.POST['query']
    if not re.fullmatch(regex, mobile):
        messages.info(request, 'Invalid Phone')
        # return redirect('contact')
    else:
        contact = Contact(name=name, email=email, mobile=mobile, query=query)
        contact.save()
        messages.info(request, 'Thankyou For Contacting us.')
    return HttpResponseRedirect(reverse('contact'))
