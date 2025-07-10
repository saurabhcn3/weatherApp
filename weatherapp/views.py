from django.shortcuts import render
import requests as re
import datetime

def home(request):
    if 'city' in request.GET:
        city = request.GET['city']
    else:
        city = 'Varanasi'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=64cfce26b676a48cbb34360a40787226&units=metric'

    response = re.get(url)
    data = response.json()
    
    if response.status_code == 200 and 'weather' in data:
        payload = {
            'city': data['name'],
            'country': data['sys']['country'],
            'today': datetime.date.today().strftime('%A %d %B %Y'),
            'description': data['weather'][0]['description'],
            'icon': f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png",
            'temp': data['main']['temp'],
            'day': datetime.date.today(),
            'pressure': data['main']['pressure'],
            'humidity': data['main']['humidity']
        }
    else:
        payload = {
            'city': city,
            'today': datetime.date.today().strftime('%A %d %B %Y'),
            'description': "City not found",
            'icon': "",
            'temp': "-",
            'day': datetime.date.today(),
            'pressure': "-",
            'humidity': "-"
        }
    return render(request, 'home.html', {'data': payload})
