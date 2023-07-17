from django.forms import ModelForm, TextInput 
from .models import USCities 

'''
Form for user to input a city
'''
class CityForm(ModelForm):
    class Meta:   
        model = USCities  
        fields=['city']    
        widgets = {'city' : TextInput(attrs={'class' : 'input' , 'placeholder': 'Find a city'})}
        
        
        
        
        
'''
Form for user to input a city
'''
class SearchForm(ModelForm):
    class Meta:   
        model = USCities  
        fields=['city']    
        widgets = {'city' : TextInput(attrs={'class' : 'input' , 'placeholder': 'Search a weather condition'})}

