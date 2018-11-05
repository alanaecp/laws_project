from django.contrib import admin

from .models import Publication

class PublicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links=('id', 'title')
    list_per_page = 25
admin.site.register(Publication, PublicationAdmin)
