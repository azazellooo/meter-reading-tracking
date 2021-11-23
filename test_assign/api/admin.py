from django.contrib import admin

from .models import Meter, History

#
@admin.register(Meter)
class MeterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'person', 'current_meter_reading']
    list_filter = ['person']
    search_fields = ['name', 'person']
    fields = ['name', 'person', 'current_meter_reading']
    readonly_fields = ['id']


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'meter', 'consumption', 'meter_reading', 'type']
    list_filter = ['type', 'date', 'meter']
    search_fields = ['meter_reading']
    fields = ['date', 'meter', 'meter_reading', 'consumption', 'type']
    readonly_fields = ['id']

# Register your models here.
