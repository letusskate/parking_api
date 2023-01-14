from django.contrib import admin
from apps.users.models import Users
# Register your models here.
@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'username', 'gender']