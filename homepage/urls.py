from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('description/<int:desc_id>', views.description, name='description'),
    path('destination', views.travel, name='travel')

]
