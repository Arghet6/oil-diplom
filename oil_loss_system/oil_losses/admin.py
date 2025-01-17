from django.contrib import admin
from .models import OilLossRecord, FuelLossCalculation, CorrosionLossCalculation, OilEvaporationLossCalculation

@admin.register(OilLossRecord)
class OilLossRecordAdmin(admin.ModelAdmin):
    list_display = ('date', 'location', 'oil_type', 'estimated_loss', 'actual_loss', 'loss_difference')
    search_fields = ('location', 'oil_type')
    list_filter = ('date', 'oil_type')

@admin.register(FuelLossCalculation)
class FuelLossCalculationAdmin(admin.ModelAdmin):
    list_display = ('date', 'volume', 'fill_time', 'vapor_pressure', 'vapor_temp', 'initial_boiling_temp', 'flow_rate', 'pressure', 'calculated_loss')
    search_fields = ('date',)
    list_filter = ('date',)

@admin.register(CorrosionLossCalculation)
class CorrosionLossCalculationAdmin(admin.ModelAdmin):
    list_display = ('date', 'diameter', 'distance_from_bottom', 'fluid_height', 'viscosity', 'duration_corrosion', 'calculated_loss')
    search_fields = ('date',)
    list_filter = ('date',)

@admin.register(OilEvaporationLossCalculation)
class OilEvaporationLossCalculationAdmin(admin.ModelAdmin):
    list_display = ('date', 'temperature', 'density_standard', 'viscosity_293', 'viscosity_323', 'duration_evaporation', 'evaporation_rate', 'area', 'calculated_loss')
    search_fields = ('date',)
    list_filter = ('date',)