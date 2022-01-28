from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.forms import CreateUser
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
    template_name = 'blog/add_post.html'
    fields = "__all__"


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'blog/update.html'
    fields = ['title', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('blog:home')


def register(request):
    form = CreateUser()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account was created for " + user)

            return redirect('blog:login')

    context = {"form": form}

    return render(
        request,
        'blog/register.html',
        context=context
    )


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('blog:home')
        else:
            messages.info(request, "Username OR password is incorrect.")

    context = {}

    return render(
        request,
        'blog/login.html',
        context=context
    )


def logout_user(request):
    logout(request)
    return redirect('blog:login')
