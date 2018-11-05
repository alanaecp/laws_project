from django.contrib import admin

from .models import Area

class AreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    list_display_links=('id', 'title')
    list_per_page = 25
admin.site.register(Area, AreaAdmin)
