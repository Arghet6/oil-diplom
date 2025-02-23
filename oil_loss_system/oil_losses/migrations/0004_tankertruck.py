# Generated by Django 5.0.7 on 2025-01-20 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oil_losses', '0003_corrosionlosscalculation_fuellosscalculation_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TankerTruck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50, verbose_name='Модель')),
                ('base_chassis', models.CharField(max_length=50, verbose_name='Базовое шасси')),
                ('length', models.IntegerField(verbose_name='Длина')),
                ('width', models.IntegerField(verbose_name='Ширина')),
                ('height', models.IntegerField(verbose_name='Высота')),
                ('operational_capacity', models.FloatField(verbose_name='Эксплуатационная вместимость')),
                ('geometric_capacity', models.FloatField(verbose_name='Геометрическая вместимость')),
                ('filling_time_with_pump', models.IntegerField(verbose_name='Время заполнения с насосом')),
                ('discharge_time_with_pump', models.IntegerField(blank=True, null=True, verbose_name='Время слива с насосом')),
                ('discharge_time_by_gravity', models.IntegerField(blank=True, null=True, verbose_name='Время слива самотоком')),
                ('tank_shape', models.CharField(blank=True, max_length=50, null=True, verbose_name='Форма цистерны')),
            ],
            options={
                'verbose_name': 'Автомобиль-цистерна',
                'verbose_name_plural': 'Автомобили-цистерны',
            },
        ),
    ]
