from django.contrib import admin
from .models import OilLossRecord

@admin.register(OilLossRecord)
class OilLossRecordAdmin(admin.ModelAdmin):
    list_display = ('date', 'location', 'oil_type', 'estimated_loss', 'actual_loss')
    search_fields = ('location', 'oil_type')
    list_filter = ('date', 'oil_type')
