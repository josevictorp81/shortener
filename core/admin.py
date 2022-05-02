from django.contrib import admin

from .models import Links

@admin.register(Links)
class LinksAdmin(admin.ModelAdmin):
    list_display = ['short_link', 'original_link']
