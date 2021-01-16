from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import PasswordInput
from django.forms.widgets import TextInput

from .models import Profile
from apps.users.models import User


# ideally wouldnt have plain text user/pw, could put in enviroment vairables but that seems overkill
class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(
        widget=TextInput(attrs={"class": "validate", "value": "DemoUser"})
    )
    password = forms.CharField(widget=PasswordInput(attrs={"value": "impassword"}))


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].initial = "default@email.com"


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio", "image", "first_name", "last_name"]
