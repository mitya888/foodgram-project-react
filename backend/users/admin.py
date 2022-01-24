from django.contrib import admin
from users.models import Follow, User
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass
    # list_display = (
    #     'id', 'username', 'email', 'first_name', 'last_name', 'password',
    # )
    # list_filter = ('username', 'email')
    # search_fields = ('username', 'email')
    # empty_value_display = '-пусто-'


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('id', 'subscriber', 'author')
    list_filter = ('subscriber', 'author')
    empty_value_display = '-пусто-'
