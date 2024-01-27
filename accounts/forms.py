from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm"
            }
        ),
    )
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(
            attrs={
                "class": "w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm"
            }
        ),
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm"
            }
        ),
    )
    password2 = forms.CharField(
        label="Password Confirmation",
        widget=forms.PasswordInput(
            attrs={
                "class": "w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm"
            }
        ),
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
