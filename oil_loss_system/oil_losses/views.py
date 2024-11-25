from django.shortcuts import render, get_object_or_404
from .models import OilLossRecord
from django.shortcuts import redirect
from .forms import OilLossRecordForm

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