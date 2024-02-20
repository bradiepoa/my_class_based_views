from django.shortcuts import render
from .models import*
from django.views.generic import ListView, DetailView,UpdateView

# Create your views here. 

class IndexView(ListView):
    model = Core
    template_name = 'core/index.html'
    context_object_name = 'index'

class SingleView(DetailView):
    model = Core
    template_name = 'core/single.html'
    context_object_name = 'post'

class PostsView(ListView):
    model = Core
    template_name = 'core/posts.html'
    context_object_name = 'post_list'