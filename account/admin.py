from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .form import CustomUserChangeForm, CustomUserCreationForm

# Register your models here.
CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser



admin.site.register(CustomUser)