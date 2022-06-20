from django.urls import path
from . import views

urlpatterns = [
    path('contact', views.contact_page, name='contact'),
    path('add_contact', views.add_contact, name='add_contact'),


]