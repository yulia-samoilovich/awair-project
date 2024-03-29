from django.shortcuts import render
from django.http import JsonResponse
from .models import AwairModel
from django.views.decorators.csrf import csrf_exempt
import json
from django.db.models import Avg

#activate virtual env: source env/bin/activate

@csrf_exempt
def consume_data(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    timestamp = body["timestamp"]
    score = body["score"]
    temp = body["temp"]
    humid = body["humid"]
    co2 = body["co2"]
    voc = body["voc"]
    pm25 = body["pm25"]

    insert_data = AwairModel.objects.create(timestamp=timestamp, score=score, temp=temp, humid=humid, co2=co2,
                                voc=voc, pm25=pm25)
    
    data = {
        'status': 'success'
    }
    return JsonResponse(data)

def display_data(request):
    all_data = AwairModel.objects.all()

    co2_data = []
    humid_data = []
    voc_data = []
    pm25_data = []
    temp_data = []

    for data in all_data:
        co2_data.append(data.co2)
        humid_data.append(data.humid)
        voc_data.append(data.voc)
        pm25_data.append(data.pm25)
        temp_data.append(data.temp)

    x_co2 = [*range(1, len(co2_data))]
    x_temp = [*range(1, len(temp_data))]
    x_voc = [*range(1, len(voc_data))]
    x_humid = [*range(1, len(humid_data))]
    x_pm25 = [*range(1, len(pm25_data))]

    return render(request, "air_quality/index.html", {"all_data":all_data,
    "co2_data":co2_data, "x_co2":x_co2, "humid_data":humid_data, "x_humid":x_humid,
    "voc_data":voc_data, "x_voc":x_voc, "pm25_data":pm25_data, "x_pm25":x_pm25, "temp_data":temp_data,
    "x_temp":x_temp})

def request_json(request):
    
    data = list(AwairModel.objects.values())

    return JsonResponse({'data':data})

def display_average(request):
    avg_co2 = AwairModel.objects.aggregate(Avg('co2'))
    avg_hum = AwairModel.objects.aggregate(Avg('humid'))
    avg_voc = AwairModel.objects.aggregate(Avg("voc"))
    avg_pm25 = AwairModel.objects.aggregate(Avg("pm25"))
    avg_temp = AwairModel.objects.aggregate(Avg("temp"))

    daily_co2 = AwairModel.objects.raw('''SELECT 1 id, strftime('%Y %m %d', timestamp) as  'date',  avg(co2) as  'avgco2'
                                                FROM 
                                                (
                                                SELECT timestamp, (SUM(co2) / COUNT(co2)) as 'co2'
                                                FROM air_quality_awairmodel
                                                GROUP BY  timestamp
                                                )
                                                GROUP BY date''')
    
    daily_temp = AwairModel.objects.raw('''SELECT 1 id, strftime('%Y %m %d', timestamp) as  'date',  avg(temp) as  'avgtemp'
                                                FROM 
                                                (
                                                SELECT timestamp, (SUM(temp) / COUNT(temp)) as 'temp'
                                                FROM air_quality_awairmodel
                                                GROUP BY  timestamp
                                                )
                                                GROUP BY date''')

    co2 = []
    for co2_data in daily_co2:
        co2.append(co2_data.avgco2)

    days = []
    for day in daily_co2:
        days.append(day.date)

    temp = []
    for temp_data in daily_temp:
        temp.append(temp_data.avgtemp)

    days_temp = []
    for day in daily_temp:
        days_temp.append(day.date)

    return render(request, "air_quality/average.html", {"days":days, "co2":co2, "avg_co2":avg_co2, "avg_hum":avg_hum, 
    "avg_voc":avg_voc, "avg_pm25":avg_pm25, "avg_temp":avg_temp, "temp":temp, "days_temp":days_temp})

