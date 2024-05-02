from django.shortcuts import render
from .models import Data

def index(request):
    data = Data.objects.all()
    context = {
        'data' : data,
    }
    return render(request, 'dataloger_app/index.html', context)
