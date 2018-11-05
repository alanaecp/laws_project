from django.contrib import admin

from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_display_links=('id', 'name')
    list_per_page = 25
admin.site.register(Member, MemberAdmin)
