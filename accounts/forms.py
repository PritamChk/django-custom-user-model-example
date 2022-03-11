from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from .models import BaseAccount

class AccountCreationForm(UserCreationForm):
    class Meta:
        mdoel = BaseAccount
        fields = ("email",'first_name','last_name')


class AccountChangeForm(UserChangeForm):
    class Meta:
        mdoel = BaseAccount
        fields = ("email",'first_name','last_name','date_joined')