from django.shortcuts import render
from .models import OilLossRecord

def index(request):
    records = OilLossRecord.objects.all()
    return render(request, 'index.html', {'records': records})
