from django.contrib import admin
from .models import SportsSpace


@admin.register(SportsSpace)
class SportsSpaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'sport_type', 'cost_per_hour')

