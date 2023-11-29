from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ["username", "email", "is_active",
                    "is_superuser", "is_staff", "date_joined"]
    list_filter = ["is_staff"]
    fieldsets = [
        ("Credentials", {"fields": ["username", "email", "password"]}),
        ("Personal info", {"fields": [
         "first_name", "last_name", "date_of_birth", "gender"]}),
        ("Permissions", {"fields": [
         "is_active", "is_staff", "is_superuser", "groups", "user_permissions"]}),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["username", "email", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = (
        "groups",
        "user_permissions",
    )
