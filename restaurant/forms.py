from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Логин',
            'class': 'auth-input'
        })
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Пароль',
            'class': 'auth-input'
        })
    )


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Логин',
            'class': 'auth-input'
        })
    )
    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Пароль',
            'class': 'auth-input'
        })
    )
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Повторите пароль',
            'class': 'auth-input'
        })
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
