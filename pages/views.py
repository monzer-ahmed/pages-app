from django.shortcuts import render
from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = 'home.html'

class About(TemplateView):
    template_name = 'about.html'