from django.shortcuts import render, get_object_or_404
from .models import OilLossRecord
from django.shortcuts import render, redirect
from .forms import OilLossRecordForm
from django.contrib.auth import login
from .forms import UserRegisterForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from .forms import FuelLossForm, CorrosionLossForm, OilEvaporationLossForm
import json
from django.http import JsonResponse
from .models import FuelLossCalculation
from .models import CorrosionLossCalculation
from .models import OilEvaporationLossCalculation

def index(request):
    oil_type = request.GET.get('oil_type')
    if oil_type:
        records = OilLossRecord.objects.filter(oil_type=oil_type)
    else:
        records = OilLossRecord.objects.all()

    context = {
        'records': records,
        'filter': oil_type,
    }
    return render(request, 'index.html', context)

def detail(request, record_id):
    record = get_object_or_404(OilLossRecord, id=record_id)
    return render(request, 'detail.html', {'record': record})


def create_record(request):
    if request.method == "POST":
        form = OilLossRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = OilLossRecordForm()

    return render(request, 'create_record.html', {'form': form})

def edit_record(request, pk):
    record = get_object_or_404(OilLossRecord, pk=pk)
    if request.method == "POST":
        form = OilLossRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = OilLossRecordForm(instance=record)
    return render(request, 'edit.html', {'form': form, 'record': record})

def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    return render(request, 'welcome.html')  # Показывает "Здарова..." для гостей

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматически вход после регистрации
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def home(request):
    # Логика для страницы "Главная"
    return render(request, 'home.html')

def calculations(request):
    # Логика для страницы расчетов
    return render(request, 'calculations.html')

def archive(request):
    # Логика для страницы архива
    return render(request, 'archive.html')

def logout_view(request):
    logout(request)  # Выход пользователя
    return redirect('login')  # Перенаправление на страницу входа
# 1
def calculate_fuel_loss(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        # Создаем новый расчет
        calculation = FuelLossCalculation(
            volume=data['volume'],
            fill_time=data['fill_time'],
            vapor_pressure=data['vapor_pressure'],
            vapor_temp=data['vapor_temp'],
            initial_boiling_temp=data['initial_boiling_temp'],
            flow_rate=data['flow_rate'],
            pressure=data['pressure'],
            calculated_loss=data['calculated_loss'],
        )

        # Сохраняем в базу данных
        calculation.save()

        # Ответ с подтверждением
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

# 2
def corrosion_loss_calculation(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        # Сохраняем данные в модели
        calculation = CorrosionLossCalculation(
            diameter=data['diameter'],
            distance_from_bottom=data['distance_from_bottom'],
            fluid_height=data['fluid_height'],
            viscosity=data['viscosity'],
            duration_corrosion=data['duration_corrosion'],
            calculated_loss=data['calculated_loss'],  # сохраняем рассчитанный объем потерь
        )
        calculation.save()

        # Отправляем ответ об успешном сохранении данных
        return JsonResponse({'success': True})

    return JsonResponse({'success': False})
# 3

def oil_evaporation_loss_calculation(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        # Создаем новый расчет, но без выполнения расчетов
        calculation = OilEvaporationLossCalculation(
            temperature=data['temperature'],
            density_standard=data['density_standard'],
            viscosity_293=data['viscosity_293'],
            viscosity_323=data['viscosity_323'],
            duration_evaporation=data['duration_evaporation'],
            evaporation_rate=data['evaporation_rate'],
            area=data['area'],
            calculated_loss=0.0,  # Здесь не выполняем расчет, сохраняем 0.0
        )

        # Сохраняем в базу данных
        calculation.save()

        # Ответ с подтверждением
        return JsonResponse({'success': True})

    return JsonResponse({'success': False, 'error': 'Invalid method'})


