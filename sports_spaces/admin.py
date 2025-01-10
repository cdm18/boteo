# sports_spaces/admin.py
from django.contrib import admin
from .models import SportsSpace, Area

class AreaInline(admin.TabularInline):
    model = Area
    extra = 1

@admin.register(SportsSpace)
class SportsSpaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'opening_time', 'closing_time')
    inlines = [AreaInline]
