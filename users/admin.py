from django.contrib import admin
from django.contrib.auth import get_user_model
from . import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
User = get_user_model()


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    search_fields = ["username"]
    add_form = forms.CustomUserCreationForm
    add_fieldsets = ((None, {"fields": ("username", "password1", "password2")}),)
    fieldsets = BaseUserAdmin.fieldsets
    model = User
    list_display = [
        "email",
        "username",
        "is_superuser",
    ]
