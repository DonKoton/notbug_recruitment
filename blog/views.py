from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.forms import PostForm, CreateUserForm
from blog.models import Post


# Create your views here.


class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    ordering = ['-modified']


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'blog/update.html'
    fields = ['title', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('blog:home')


class CreateUserView(CreateView):
    form_class = CreateUserForm
    success_url = reverse_lazy('blog:home')
    template_name = 'blog/register.html'
