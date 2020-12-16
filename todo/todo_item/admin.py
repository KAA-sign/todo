from django.contrib import admin
from todo_item.models import ItemModel


class ListAdmin(admin.ModelAdmin):
    list_display = ['id', 'created', 'name', 'is_done', 'expare_date']
    list_filter = ['created', 'name', 'is_done']
    search_fields = ['name', 'user']


admin.site.register(ItemModel, ListAdmin)
