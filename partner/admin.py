from partner.models import UserProfile

__author__ = 'Harvey'

from django.contrib import admin

class UserProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(UserProfile, UserProfileAdmin)
