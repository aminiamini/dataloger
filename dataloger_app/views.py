from django.shortcuts import render
from .models import Data
from django.http import HttpResponse
from datetime import datetime

def index(request):
    data = Data.objects.all()
    context = {
        'data' : data,
    }
    return render(request, 'dataloger_app/index.html', context)

def get_data(request):
    if (request.method == "POST"):

        print(request)
        temprature = request.POST['Temprature']
        humidity = request.POST['Humidity']
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%d %H:%M")

        data = Data(temprature=temprature,humidity=humidity,time=date_time)
        data.save()
        print(temprature, humidity)
        return HttpResponse("succecfully recieved and saved data!")
    else:
        return HttpResponse("Somthing wrong happend!")
