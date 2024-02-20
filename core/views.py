from django.shortcuts import render
from .models import*
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from . forms import PostForm

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


class AddView(CreateView):
    model = Core
    template_name = 'core/add.html'
    fields = '__all__'
    success_url = reverse_lazy('core:post')


class EditView(UpdateView):
    model = Core
    template_name = 'core/edit.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('core:post')

class DeleteView(DeleteView):
    model = Core
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('core:post')
    template_name = 'core/confirm_delete.html'
    