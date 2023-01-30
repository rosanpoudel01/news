from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from news.models import News, Category

User = get_user_model()


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass


# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title", "category__name")


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ("name",)
