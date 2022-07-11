from django.urls import re_path as url
from calcu_app import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
]
