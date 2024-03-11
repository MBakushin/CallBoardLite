from django.contrib import admin
from .models import *


class AnnounceAdmin(admin.ModelAdmin):
    list_display = ('id', 'header', 'text', 'time_to_create')
    list_filter = ('id', 'header', 'time_to_create')
    search_fields = ('id', 'header', 'time_to_create')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('id', 'title')
    search_fields = ('id', 'title')


admin.site.register(Announce, AnnounceAdmin)
admin.site.register(Category)
admin.site.register(Respond)
