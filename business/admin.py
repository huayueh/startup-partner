from business.models import Business

__author__ = 'Harvey'

from django.contrib import admin

class BusinessAdmin(admin.ModelAdmin):
    pass
admin.site.register(Business, BusinessAdmin)
