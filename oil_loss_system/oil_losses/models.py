from django.db import models

class OilLossRecord(models.Model):
    date = models.DateField(verbose_name="Дата")
    location = models.CharField(max_length=255, verbose_name="Местоположение")
    oil_type = models.CharField(max_length=100, verbose_name="Тип нефти или нефтепродукта")
    estimated_loss = models.FloatField(verbose_name="Оценочная потеря (тонн)")
    actual_loss = models.FloatField(verbose_name="Фактическая потеря (тонн)")

    def __str__(self):
        return f"{self.date} - {self.location} ({self.oil_type})"

    class Meta:
        verbose_name = "Запись о потере нефти"
        verbose_name_plural = "Записи о потерях нефти"
