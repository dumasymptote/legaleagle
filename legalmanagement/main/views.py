from django.shortcuts import render
from django.views import generic


# Create your views here.
class HomeView(generic.TemplateView):
    template_name = 'main/home.html'

class DashboardView(generic.TemplateView):
    template_name='main/dashboard.html'