from django.contrib import admin
from reserved.models import Table

# Register your models here.
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','image',)
    list_display_links = ('id',)