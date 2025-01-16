from django.contrib import admin
from JwtAuthenticationConfig.models import User

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')
