from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Account


class CustomUserCreationForm(UserCreationForm):
    #user_type = forms.CharField(max_length=50)

    class Meta:
        model = Account
        fields = ('email', 'username', 'user_type')


class CustomUserChangeForm(UserChangeForm):
    #user_type = forms.CharField(max_length=50)

    class Meta:
        model = Account
        fields = ('email', 'username', 'user_type')
