from django.urls import path
from . import views
from .views import calculate_fuel_loss
from .views import corrosion_loss_calculation
from .views import oil_evaporation_loss_calculation

urlpatterns = [
    path('', views.index, name='index'),
    path('record/<int:record_id>/', views.detail, name='detail'),
    path('record/new/', views.create_record, name='create_record'),
    path('record/<int:pk>/edit/', views.edit_record, name='edit_record'),  # Edit record URL
    path('create/', views.create_record, name='create_record'),
    path('home/', views.home, name='home'),
    path('calculations/', views.calculations, name='calculations'),
    path('archive/', views.archive, name='archive'),
    path('logout/', views.logout_view, name='logout'),  # Путь для выхода
    path('calculate_fuel_loss/', calculate_fuel_loss, name='calculate_fuel_loss'),
    path('corrosion_loss_calculation/', corrosion_loss_calculation, name='corrosion_loss_calculation'),
    path('oil_evaporation_loss_calculation/', oil_evaporation_loss_calculation, name='oil_evaporation_loss_calculation'),
    path('archive/', views.archive, name='archive'),
    path('fuel_loss_detail/<int:id>/', views.fuel_loss_detail, name='fuel_loss_detail'),
    path('corrosion_loss_detail/<int:id>/', views.corrosion_loss_detail, name='corrosion_loss_detail'),
    path('oil_evaporation_loss_detail/<int:id>/', views.oil_evaporation_loss_detail, name='oil_evaporation_loss_detail'),
    path('export_csv/', views.export_csv, name='export_csv'),
    path('export_excel/', views.export_excel, name='export_excel'),
]

