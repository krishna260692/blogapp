from django.shortcuts import render
from django.views.generic import TemplateView ,ListView ,DetailView
from django.views.generic.edit import CreateView,UpdateView ,DeleteView

from .models import Post, Newpost
from django.urls import reverse_lazy


# Create your views here.

class Home(TemplateView):
    template_name = 'mypost/home.html'





class Mypost(ListView):
    model = Newpost

    template_name = 'mypost/about.html'


class Mynewpost(ListView):
    model = Newpost
    template_name = 'mypost/post.html'
    context_object_name = 'all_posts_list'


class Deatilview(DetailView):
    model = Newpost
    template_name = 'mypost/deatils.html'
    context_object_name = 'indiv_post'

class BlogCreateView(CreateView):
    model = Newpost
    template_name = 'mypost/post_new.html'
    fields = '__all__'


class Blogupdateview(UpdateView):
    model = Newpost
    fields = ['title', 'body']
    template_name = 'mypost/edit.html'


class BlogDeleteView(DeleteView): # new
    model = Newpost
    template_name = 'mypost/delete.html'
    success_url = reverse_lazy('home')



