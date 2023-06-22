from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'last_login')
    search_fields = ['username']
    list_filter = (('last_login', DateFieldListFilter),)
