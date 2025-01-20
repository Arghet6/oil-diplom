import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oil-loss_system.settings')
django.setup()

from .models import TankerTruck

data = [
    {
        "model": "АЦМ-4-15ТК",
        "base_chassis": "ЗИЛ-15ТК",
        "length": 6754,
        "width": 2268,
        "height": 1497,
        "operational_capacity": 4.0,
        "geometric_capacity": 4.080,
        "filling_time_with_pump": 12,
        "discharge_time_with_pump": 10,
        "discharge_time_by_gravity": 15,
        "tank_shape": None
    },
    # Добавьте остальные записи аналогично
]

for item in data:
    TankerTruck.objects.create(**item)

print("Данные успешно загружены!")