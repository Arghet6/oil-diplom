from django.shortcuts import render, get_object_or_404
from .models import OilLossRecord
from django.shortcuts import render, redirect
from .forms import OilLossRecordForm
from django.contrib.auth import login
from .forms import UserRegisterForm
from django.contrib.auth import logout
from django.shortcuts import redirect

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

