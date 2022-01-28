from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from blog.models import Post


class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        widgets = {
            'author': forms.TextInput(attrs={"placeholder": "enter your username"}),
            'title': forms.TextInput(attrs={"placeholder": "enter title"}),
            'date': forms.TextInput(attrs={"placeholder": "YYYY-MM-DD"}),
            'body': forms.Textarea(attrs={"cols": 30, "rows": 20}),
        }
