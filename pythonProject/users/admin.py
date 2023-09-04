from django.contrib import admin
from main.admin import BasketAdmin
from users.models import User
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    inlines = (BasketAdmin, )
# Register your models here.
