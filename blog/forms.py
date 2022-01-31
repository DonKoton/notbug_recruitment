from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from blog.models import Post


class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {'class': 'form-control', 'placeholder': 'enter your username',
                                                 'required': 'required'}
        self.fields['email'].widget.attrs = {'class': 'form-control', 'placeholder': 'enter e-mail address',
                                                 'required': 'required'}
        self.fields['password1'].widget.attrs = {'class': 'form-control', 'placeholder': 'password',
                                                 'required': 'required'}
        self.fields['password2'].widget.attrs = {'class': 'form-control', 'placeholder': 'confirm password',
                                                 'required': 'required'}

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            "username": "Username",
            "email": "E-mail address",
            "password1": "Password",
            "password2": "Password confirmation",
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        widgets = {
            'author': forms.Select(attrs={
                "placeholder": "enter your username",
                "class": "form-control"
            }),
            'title': forms.TextInput(attrs={
                "placeholder": "enter title",
                "class": "form-control"
            }),
            'date': forms.TextInput(attrs={
                "placeholder": "YYYY-MM-DD",
                "class": "form-control"
            }),
            'body': forms.Textarea(attrs={
                "cols": 30, "rows": 9,
                "class": "form-control"
            }),
        }
