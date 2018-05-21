from django.contrib import admin

# Register your models here.
from user import models

class UserAdmin(admin.ModelAdmin):
    list_display = ("user_name","user_nickname","user_email","user_is_del","user_create_time")

admin.site.register(models.User,UserAdmin)
