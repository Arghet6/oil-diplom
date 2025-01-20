from django.contrib import admin
from .models import FuelLossCalculation, CorrosionLossCalculation, OilEvaporationLossCalculation, TankerTruck, DensityData

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



@admin.register(TankerTruck)
class TankerTruckAdmin(admin.ModelAdmin):
    list_display = ('model', 'base_chassis', 'length', 'width', 'height', 'operational_capacity', 'geometric_capacity', 'filling_time_with_pump', 'discharge_time_with_pump', 'discharge_time_by_gravity', 'tank_shape')
    search_fields = ('model', 'base_chassis')
    list_filter = ('base_chassis',)

@admin.register(DensityData)
class DensityDataAdmin(admin.ModelAdmin):
    list_display = ('density_range_1', 'temp_correction_1', 'expansion_coefficient_1', 'density_range_2', 'temp_correction_2', 'expansion_coefficient_2')
    search_fields = ('density_range_1', 'density_range_2')
    list_filter = ('density_range_1', 'density_range_2')