from django.urls import path
from . import views

urlpatterns = [
    path('testimonial/create/', views.create_testimonial, name='create_testimonial'),
    path('list/', views.testimonial_list, name='testimonial_list'),
]
