from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm"
            }
        ),
    )
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(
            attrs={
                "class": "mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm"
            }
        ),
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm"
            }
        ),
    )
    password2 = forms.CharField(
        label="Password Confirmation",
        widget=forms.PasswordInput(
            attrs={
                "class": "mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm"
            }
        ),
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
