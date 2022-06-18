from django.shortcuts import render
import json
import urllib.request
# Create your views here.
def index(request):
    if request.method =='POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=a515be6fa827fe2046f8f6c608b2ffe0').read()
        json_data =json.loads(res)
        data ={
            'country': str(json_data['sys']['country']),
            'coordinate': str(json_data['coord']['lon'] ) + '' + str(json_data['coord']['lat']),
            'temp': str(json_data['main']['temp'])+'k',
            'pressure': str(json_data['main']['pressure']),
            'humidity': str(json_data['main']['humidity']),
               }
    else:
        data = {}

    return render(request,'index.html',data)