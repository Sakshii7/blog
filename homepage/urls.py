from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('description/<int:id>', views.description, name='description'),
    path('destination', views.destination, name='destination')

]
