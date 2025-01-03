# Generated by Django 3.2.25 on 2024-11-25 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OilLossRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('location', models.CharField(max_length=255, verbose_name='Местоположение')),
                ('oil_type', models.CharField(max_length=100, verbose_name='Тип нефти или нефтепродукта')),
                ('estimated_loss', models.FloatField(verbose_name='Оценочная потеря (тонн)')),
                ('actual_loss', models.FloatField(verbose_name='Фактическая потеря (тонн)')),
            ],
            options={
                'verbose_name': 'Запись о потере нефти',
                'verbose_name_plural': 'Записи о потерях нефти',
            },
        ),
    ]
