from django.db import models

class OilLossRecord(models.Model):
    date = models.DateField(verbose_name="Дата")
    location = models.CharField(max_length=255, verbose_name="Местоположение")
    oil_type = models.CharField(
        max_length=100,
        choices=[
            ('Light', 'Лёгкая нефть'),
            ('Heavy', 'Тяжёлая нефть'),
            ('Gasoline', 'Бензин'),
            ('Diesel', 'Дизельное топливо'),
        ],
        verbose_name="Тип нефти или нефтепродукта",
    )
    estimated_loss = models.FloatField(verbose_name="Оценочная потеря (тонн)")
    actual_loss = models.FloatField(verbose_name="Фактическая потеря (тонн)")
    description = models.TextField(blank=True, verbose_name="Описание")

    def loss_difference(self):
        return self.estimated_loss - self.actual_loss

    def __str__(self):
        return f"{self.date} - {self.location} ({self.oil_type})"

    class Meta:
        verbose_name = "Запись о потере нефти"
        verbose_name_plural = "Записи о потерях нефти"
        ordering = ['-date']

# 1
class FuelLossCalculation(models.Model):
    date = models.DateField(verbose_name="Дата расчета", auto_now_add=True)
    volume = models.FloatField(verbose_name="Объём цистерны (м³)")
    fill_time = models.FloatField(verbose_name="Время налива цистерны (часы)")
    vapor_pressure = models.FloatField(verbose_name="Давление насыщенных паров бензина (Па)")
    vapor_temp = models.FloatField(verbose_name="Температура бензина при наливе (К)")
    initial_boiling_temp = models.FloatField(verbose_name="Температура начала кипения (К)")
    flow_rate = models.FloatField(verbose_name="Расход налива (м³/ч)")
    pressure = models.FloatField(verbose_name="Атмосферное давление (Па)")
    calculated_loss = models.FloatField(verbose_name="Рассчитанные потери (кг)", blank=True, null=True)

    def __str__(self):
        return f"Расчет от {self.date}"

    class Meta:
        verbose_name = "Расчет потерь бензина при наливе"
        verbose_name_plural = "Расчеты потерь бензина при наливе"

# 2
class CorrosionLossCalculation(models.Model):
    date = models.DateField(verbose_name="Дата расчета", auto_now_add=True)
    diameter = models.FloatField(verbose_name="Диаметр отверстия (мм)")
    distance_from_bottom = models.FloatField(verbose_name="Расстояние от дна (м)")
    fluid_height = models.FloatField(verbose_name="Уровень жидкости (м)")
    viscosity = models.FloatField(verbose_name="Кинематическая вязкость (м²/с)")
    duration_corrosion = models.FloatField(verbose_name="Время истечения (часы)")
    calculated_loss = models.FloatField(verbose_name="Рассчитанные потери (м³)", blank=True, null=True)

    def __str__(self):
        return f"Расчет от {self.date}"

    class Meta:
        verbose_name = "Расчет потерь через коррозионный свищ"
        verbose_name_plural = "Расчеты потерь через коррозионный свищ"


# 3
class OilEvaporationLossCalculation(models.Model):
    date = models.DateField(verbose_name="Дата расчета", auto_now_add=True)
    temperature = models.FloatField(verbose_name="Температура нефти (К)")
    density_standard = models.FloatField(verbose_name="Плотность нефти при стандартных условиях (кг/м³)")
    viscosity_293 = models.FloatField(verbose_name="Кинематическая вязкость нефти при 293К (м²/с)")
    viscosity_323 = models.FloatField(verbose_name="Кинематическая вязкость нефти при 323К (м²/с)")
    duration_evaporation = models.FloatField(verbose_name="Продолжительность испарения (часы)")
    evaporation_rate = models.FloatField(verbose_name="Скорость ветра (м/с)")
    area = models.FloatField(verbose_name="Площадь испарения (м²)")
    calculated_loss = models.FloatField(verbose_name="Рассчитанные потери (кг)", blank=True, null=True)

    def __str__(self):
        return f"Расчет от {self.date}"

    class Meta:
        verbose_name = "Расчет потерь нефти от испарения"
        verbose_name_plural = "Расчеты потерь нефти от испарения"

class TankerTruck(models.Model):
    model = models.CharField(max_length=50, verbose_name="Модель")
    base_chassis = models.CharField(max_length=50, verbose_name="Базовое шасси")
    length = models.IntegerField(verbose_name="Длина")
    width = models.IntegerField(verbose_name="Ширина")
    height = models.IntegerField(verbose_name="Высота")
    operational_capacity = models.FloatField(verbose_name="Эксплуатационная вместимость")
    geometric_capacity = models.FloatField(verbose_name="Геометрическая вместимость")
    filling_time_with_pump = models.IntegerField(verbose_name="Время заполнения с насосом")
    discharge_time_with_pump = models.IntegerField(verbose_name="Время слива с насосом", null=True, blank=True)
    discharge_time_by_gravity = models.IntegerField(verbose_name="Время слива самотоком", null=True, blank=True)
    tank_shape = models.CharField(max_length=50, verbose_name="Форма цистерны", null=True, blank=True)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = "Автомобиль-цистерна"
        verbose_name_plural = "Автомобили-цистерны"


class DensityData(models.Model):
    density_range_1 = models.CharField(max_length=50, verbose_name="Плотность 1 (кг/м³)")
    temp_correction_1 = models.FloatField(verbose_name="Температурная поправка 1 (кг/(м³·К))")
    expansion_coefficient_1 = models.FloatField(verbose_name="Коэффициент объемного расширения 1 (1/K)")
    density_range_2 = models.CharField(max_length=50, verbose_name="Плотность 2 (кг/м³)")
    temp_correction_2 = models.FloatField(verbose_name="Температурная поправка 2 (кг/(м³·К))")
    expansion_coefficient_2 = models.FloatField(verbose_name="Коэффициент объемного расширения 2 (1/K)")

    def __str__(self):
        return f"{self.density_range_1} - {self.density_range_2}"

    class Meta:
        verbose_name = "Данные плотности"
        verbose_name_plural = "Данные плотности"