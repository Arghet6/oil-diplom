# Generated by Django 5.0.7 on 2025-01-20 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oil_losses', '0004_tankertruck'),
    ]

    operations = [
        migrations.CreateModel(
            name='DensityData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('density_range_1', models.CharField(max_length=50, verbose_name='Плотность 1 (кг/м³)')),
                ('temp_correction_1', models.FloatField(verbose_name='Температурная поправка 1 (кг/(м³·К))')),
                ('expansion_coefficient_1', models.FloatField(verbose_name='Коэффициент объемного расширения 1 (1/K)')),
                ('density_range_2', models.CharField(max_length=50, verbose_name='Плотность 2 (кг/м³)')),
                ('temp_correction_2', models.FloatField(verbose_name='Температурная поправка 2 (кг/(м³·К))')),
                ('expansion_coefficient_2', models.FloatField(verbose_name='Коэффициент объемного расширения 2 (1/K)')),
            ],
            options={
                'verbose_name': 'Данные плотности',
                'verbose_name_plural': 'Данные плотности',
            },
        ),
    ]
