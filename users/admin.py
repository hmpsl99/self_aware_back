from django.contrib import admin
from .models import User, OTPRequest
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(OTPRequest)

@admin.register(User)
class appUserAdmin(UserAdmin):
    pass
