from django.shortcuts import render
from .models import*
from django.views.generic import ListView, DetailView,UpdateView

# Create your views here.

class IndexView(ListView):
    model = Core
    template_name = 'core/index.html'
