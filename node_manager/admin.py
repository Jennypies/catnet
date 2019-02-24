from django.contrib import admin
from .models import Node, Photo


class NodeAdmin(admin.ModelAdmin):
    readonly_fields = ['last_contact']
    filter_horizontal = ['contacts']


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['pub_date', 'node', 'photo']
    list_filter = ['node']
    date_hierarchy = 'pub_date'


admin.site.register(Node, NodeAdmin)
admin.site.register(Photo, PhotoAdmin)
