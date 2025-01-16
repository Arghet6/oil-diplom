# Generated by Django 5.1.4 on 2025-01-16 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oil_losses', '0002_alter_oillossrecord_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CorrosionLossCalculation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата расчета')),
                ('diameter', models.FloatField(verbose_name='Диаметр отверстия (мм)')),
                ('distance_from_bottom', models.FloatField(verbose_name='Расстояние от дна (м)')),
                ('fluid_height', models.FloatField(verbose_name='Уровень жидкости (м)')),
                ('viscosity', models.FloatField(verbose_name='Кинематическая вязкость (м²/с)')),
                ('duration', models.FloatField(verbose_name='Время истечения (часы)')),
                ('calculated_loss', models.FloatField(blank=True, null=True, verbose_name='Рассчитанные потери (м³)')),
            ],
            options={
                'verbose_name': 'Расчет потерь через коррозионный свищ',
                'verbose_name_plural': 'Расчеты потерь через коррозионный свищ',
            },
        ),
        migrations.CreateModel(
            name='FuelLossCalculation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата расчета')),
                ('volume', models.FloatField(verbose_name='Объём цистерны (м³)')),
                ('fill_time', models.FloatField(verbose_name='Время налива цистерны (часы)')),
                ('vapor_pressure', models.FloatField(verbose_name='Давление насыщенных паров бензина (Па)')),
                ('vapor_temp', models.FloatField(verbose_name='Температура бензина при наливе (К)')),
                ('initial_boiling_temp', models.FloatField(verbose_name='Температура начала кипения (К)')),
                ('flow_rate', models.FloatField(verbose_name='Расход налива (м³/ч)')),
                ('pressure', models.FloatField(verbose_name='Атмосферное давление (Па)')),
                ('calculated_loss', models.FloatField(blank=True, null=True, verbose_name='Рассчитанные потери (кг)')),
            ],
            options={
                'verbose_name': 'Расчет потерь бензина при наливе',
                'verbose_name_plural': 'Расчеты потерь бензина при наливе',
            },
        ),
        migrations.CreateModel(
            name='OilEvaporationLossCalculation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата расчета')),
                ('temperature', models.FloatField(verbose_name='Температура нефти (К)')),
                ('density_standard', models.FloatField(verbose_name='Плотность нефти при стандартных условиях (кг/м³)')),
                ('viscosity_293', models.FloatField(verbose_name='Кинематическая вязкость нефти при 293К (м²/с)')),
                ('viscosity_323', models.FloatField(verbose_name='Кинематическая вязкость нефти при 323К (м²/с)')),
                ('duration', models.FloatField(verbose_name='Продолжительность испарения (часы)')),
                ('evaporation_rate', models.FloatField(verbose_name='Скорость ветра (м/с)')),
                ('area', models.FloatField(verbose_name='Площадь испарения (м²)')),
                ('calculated_loss', models.FloatField(blank=True, null=True, verbose_name='Рассчитанные потери (кг)')),
            ],
            options={
                'verbose_name': 'Расчет потерь нефти от испарения',
                'verbose_name_plural': 'Расчеты потерь нефти от испарения',
            },
        ),
    ]
