from django.contrib import admin
from .models import MiniURL
# Register your models here.


class MiniURLAdmin(admin.ModelAdmin):
    list_display = ('default_url', 'url_code', 'create_at', 'identifier_create', 'access_number')
    list_filter = ('identifier_create', )
    date_hierarchy = 'create_at'
    ordering = ('create_at', )
    search_fields = ('default_url', )

admin.site.register(MiniURL, MiniURLAdmin)