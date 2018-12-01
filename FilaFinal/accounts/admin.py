from django.contrib import admin
from .models import *

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_info')

    def user_info(self, obj):
        return obj.descriere

admin.site.register(UserProfile, UserProfileAdmin)
# Register your models here.
