from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User, Profile, Post, PostImage, Comment, Reply


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ["username", "email", "is_active",
                    "is_superuser", "is_staff", "date_joined"]
    list_filter = ["is_staff"]
    fieldsets = [
        ("Credentials", {"fields": ["username", "email", "password"]}),
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


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "text", "like_counts", "dislike_counts"]

    fieldsets = [
        (None, {"fields": ["profile", "text"]}),
    ]


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ["id", "image"]


@admin.register(Comment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = ["id", "text", "like_counts", "dislike_counts"]
    
    fieldsets = [
        (None, {"fields": ["post", "text"]}),
    ]


@admin.register(Reply)
class PostReplyCommentAdmin(admin.ModelAdmin):
    list_display = ["id", "text", "like_counts", "dislike_counts"]
    
    fieldsets = [
        (None, {"fields": ["comment", "text"]}),
    ]


admin.site.register(Profile)
