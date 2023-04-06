from django.shortcuts import render
import requests
import datetime
# Create your views here.
def index(request):

    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Hungary'

    appid = '9dcfcb1ced163482cd63c98b4159b432'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PAR= {'q':city, 'appid':appid, 'units':'metric'}
    r = requests.get(url=URL, params=PAR)
    res = r.json()
    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']

    day = datetime.date.today()

    return render(request, 'WeatherApp/index.html', {'description':description, 'icon':icon, 'temp':temp, 'day':day, 'city':city})