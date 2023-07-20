import requests
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import USCities
from .resources import USCitiesResource
from django.contrib import messages
from tablib import Dataset
import environ
import sheets
from django.core.paginator import Paginator
from .forms import CityForm, SearchForm
from django.views import View
env = environ.Env()
environ.Env.read_env()




def simple_upload(request):
    '''  
    Upload a xlsx file to djangos database to create objects based on the model USCities 
    '''
    if request.method == 'POST':
        cities_resource = USCitiesResource()
        dataset = Dataset()
        new_city = request.FILES['myfile']
        if not new_city.name.endswith('xlsx'):
            return render(request, 'upload.html')
        
        imported_data = dataset.load(new_city.read(), format='xlsx')
        for data in imported_data:
            value = USCities(data[0], data[1], data[2])
            value.save()
    return render(request, 'upload.html')


''' DEVELOPMENT '''
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=d3b3bb0d790b988a85dae5805dc23153'  # accessing Open Weathers API, use given (Chetram Bassit's) API key

''' PRODUCTION '''
# WEATHERAPIKEY = env("WEATHERAPIKEY") 
# url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={WEATHERAPIKEY}'  # USE IN PRODUCTION !



class IndexView(View):
    
    def get(self, request):
        ''' 
        Get all objects from USCities model, paginate objects, access open weather api to get specific data needed for specific city,
        append data into a list.
        '''
        p = Paginator(USCities.objects.all(), 10)
        page = request.GET.get("page")
        cities = p.get_page(page)
        weather_data = []
        for city in cities:
            r = requests.get(url.format(city)).json()
            if 'main' and 'wind' and 'weather' in r:

                city_weather = {
                    'city' : city.city,
                    'temperature' :  r['main']['temp'],
                    'wind': r['wind']['speed'],
                    'description' : r['weather'][0]['description'],
                    'icon' : r['weather'][0]['icon'],
                }
                
            else:
                print('Error')
            weather_data.append(city_weather)
            
        form = CityForm()
        context = {
            'weather_data' : weather_data, 
            'cities': cities,
            'form' : form,
            
        }

        return render(request, 'home.html', context)
    
    
    def post(self, request):
        ''' 
            Enter a city name into the form, check open weathers api for cities existence, if city exists add to database 
        '''
        err_msg = ''
        success_msg = ''
        message = ''
        message_class = ''

        if request.method == 'POST':
            form = CityForm(request.POST)

            if form.is_valid():
                new_city = form.cleaned_data['city']
                existing_city_count = USCities.objects.filter(city=new_city).count()
                
                if existing_city_count == 0:
                    r = requests.get(url.format(new_city)).json()

                    if r['cod'] == 200:
                        form.save()
                    elif r['cod'] != 200:
                        err_msg = 'City does not exist!'
                        
                else:
                    success_msg = 'Found the city in our database!'

                if err_msg:
                    message = err_msg
                    message_class = 'is-danger'
                else:
                    message = success_msg
                    message_class = 'is-success'
        form = CityForm()

        weather_data = []
        r = requests.get(url.format(new_city)).json()
        
        if 'main' and 'wind' and 'weather' in r:
            city_weather = {
                'city' : new_city,
                'temperature' :  r['main']['temp'],
                'wind': r['wind']['speed'],
                'description' : r['weather'][0]['description'],
                'icon' : r['weather'][0]['icon'],
            }
            weather_data.append(city_weather)
        else:
            print('Error')

        context = {
            'weather_data' : weather_data, 
            'form' : form,
            'message' : message,
            'message_class' : message_class
        }

        return render(request, 'home.html', context)



class SearchWeather(View):
    def get(self, request, *args, **kwargs):      
        '''
        Access all cities from USCities objects experiencing weather condition based on User input
        '''
        query = self.request.GET.get("query")
        weather_data= []
        
        cities = USCities.objects.all()
        for city in cities:
            r = requests.get(url.format(city)).json()
            if 'main' and 'wind' and 'weather' in r:
                city_weather = {
                    'city' : city.city,
                    'temperature' :  r['main']['temp'],
                    'wind': r['wind']['speed'],
                    'description' : r['weather'][0]['description'],
                    'icon' : r['weather'][0]['icon'],
                }
            else:
                print('Error')
                
            if query in city_weather.values():
                weather_data.append(city_weather)
    
        p = Paginator(weather_data, 5)
        page = request.GET.get("page")
        cities = p.get_page(page)
        context = {
            "weather_data": weather_data,
            "query": query,
            "cities": cities,
        }
        return render(request, "weather_search.html", context)
    
    
def delete_city(request, city_name):
    USCities.objects.get(city=city_name).delete()
    return redirect('home')

