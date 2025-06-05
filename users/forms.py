from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from typing import Union

from .models import MailRequest
User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields= (
            "email",
            "username",
        )




class MailRequestForm(forms.ModelForm):
    class Meta:       
        model = MailRequest
        fields = ['email', 'message']
        widgets: dict[str, Union[forms.EmailInput, forms.Textarea]] = {
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "message": forms.Textarea(attrs={"class": "form-control"}),
        }

