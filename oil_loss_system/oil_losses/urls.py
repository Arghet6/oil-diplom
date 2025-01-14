from django.urls import path
from . import views

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
]