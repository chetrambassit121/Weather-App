from django.shortcuts import render, redirect
from .models import USCities
from .resources import USCitiesResource
from django.contrib import messages
from tablib import Dataset


'''  
Upload a xlsx file to djangos database to create objects based on the model USCities 
Package/Library Requirements: django-import-export
Required Files: resources.py
'''
def simple_upload(request):
    if request.method == 'POST':
        cities_resource = USCitiesResource()
        dataset = Dataset()
        new_city = request.FILES['myfile']
        
        if not new_city.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request, 'weather/upload.html')
        
        imported_data = dataset.load(new_city.read(), format='xlsx')
        for data in imported_data:
            value = USCities(data[0], data[1], data[2])
            value.save()
    return render(request, 'upload.html')