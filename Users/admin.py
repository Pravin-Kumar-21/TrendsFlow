from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


# Register your models here.
from . import models


@admin.register(models.User)
class UserDash(admin.ModelAdmin):
    """Custom User Admin"""

    list_display = (
        "first_name",
        "last_name",
        "last_name",
        "avatar",
        "language",
    )
